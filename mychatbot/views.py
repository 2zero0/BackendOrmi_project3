from django.shortcuts import render
from django.views import View
import os
from dotenv import load_dotenv
import openai
from .models import Conversation, ChatRequestCounter
from chatlog.models import ChatMessage  # chatlog 앱의 모델
# json
from django.http import JsonResponse
import json
# DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
import datetime

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

### View
# class ChatbotView(View):
#     def get(self, request, *args, **kwargs):
#         conversations = request.session.get('conversations', [])
#         return render(request, 'chat.html', {'conversations': conversations})

#     def post(self, request, *args, **kwargs):
#         # 자바스크립트와 통신
#         data = json.loads(request.body)
#         prompt = data.get('prompt')

#         # prompt = request.POST.get('prompt')
#         if prompt:
#             # 이전 대화 기록 가져오기
#             session_conversations = request.session.get('conversations', [])
#             previous_conversations = "\n".join([f"User: {c['prompt']}\nAI: {c['response']}" for c in session_conversations])
#             prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"

#             model_engine = "text-davinci-003"
#             completions = openai.Completion.create(
#                 engine=model_engine,
#                 prompt=prompt_with_previous,
#                 max_tokens=1024,
#                 n=5,
#                 stop=None,
#                 temperature=0.5,
#             )
#             response = completions.choices[0].text.strip()

#             # DB에 추가
#             conversation = Conversation(prompt=prompt, response=response)
#             conversation.save()

#             ## conversation = {'prompt': prompt, 'response': response}

#             ## 대화 기록에 새로운 응답 추가
#             ## session_conversations.append(conversation)
#             ## request.session['conversations'] = session_conversations

#             # 대화 기록에 새로운 응답 추가 (수정된 코드)
#             session_conversations.append({'prompt': prompt, 'response': response})
#             request.session['conversations'] = session_conversations
#             request.session.modified = True

#             ## ChatMessage 모델에 대화 내역 저장
#             ## conversation_content = f"prompt: {prompt} / response: {response}"
#             ## chat_message = ChatMessage(sender=request.user, content=conversation_content)
#             ## chat_message.save()

#             # 기존 html-js 프로젝트와 통신 위한 코드
#             # JsonResponse로 응답 data를 보내기
#             res_data = {'choices': [{'message': {'content': response}}]}
#             return JsonResponse(res_data)
        
#         else:
#             return JsonResponse({"error": "No prompt provided"}, status=400)


### DRF
class ChatbotAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        today = datetime.date.today()
        try:
            chat_request_counter = ChatRequestCounter.objects.get(user=user, date=today)
        except ObjectDoesNotExist:
            chat_request_counter = ChatRequestCounter(user=user, date=today)
            chat_request_counter.save()

        if chat_request_counter.count >= 5:
            return Response({"error": "하루 5회 요청 제한에 도달했습니다."}, status=status.HTTP_429_TOO_MANY_REQUESTS)

        chat_request_counter.count += 1
        chat_request_counter.save()

        # 자바스크립트와 통신
        # data = json.loads(request.body)
        # prompt = data.get('prompt')
        prompt = request.data.get('prompt')

        if prompt:
            # 이전 대화 기록 가져오기
            session_conversations = request.session.get('conversations', [])
            previous_conversations = "\n".join([f"User: {c['prompt']}\nAI: {c['response']}" for c in session_conversations])
            prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"

            model_engine = "text-davinci-003"
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt_with_previous,
                max_tokens=1024,
                n=5,
                stop=None,
                temperature=0.5,
            )
            response = completions.choices[0].text.strip()

            # DB에 추가
            conversation = Conversation(prompt=prompt, response=response)
            conversation.save()

            # 세션 내용이 변했음을 감지 -> 변경 내용 DB 저장
            session_conversations.append({'prompt': prompt, 'response': response})
            request.session['conversations'] = session_conversations
            request.session.modified = True

            recent_user_prompt = None
            for item in reversed(prompt):
                if item['role'] == 'user':
                    recent_user_prompt = item['content']
                    break

            # ChatMessage 모델에 사용자 정보, 질문, 답변 저장
            chat_message = ChatMessage(sender=request.user, prompt=recent_user_prompt, response=response)
            chat_message.save()

            ## 기존 html-js 프로젝트와 통신 위한 코드
            # JsonResponse로 응답 data를 보내기
            res_data = {'choices': [{'message': {'content': response}}]}
            return Response(res_data)
        
        else:
            return Response({"error": "No prompt provided"}, status=status.HTTP_400_BAD_REQUEST)