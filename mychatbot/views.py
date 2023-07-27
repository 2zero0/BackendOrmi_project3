from django.shortcuts import render
from django.views import View
import os
from dotenv import load_dotenv
import openai
from .models import Conversation
from chatlog.models import ChatMessage  # chatlog 앱 - ChatMessage 모델

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


class ChatbotView(View):
    def get(self, request, *args, **kwargs):
        conversations = request.session.get('conversations', [])
        return render(request, 'chat.html', {'conversations': conversations})

    def post(self, request, *args, **kwargs):
        prompt = request.POST.get('prompt')
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

            # conversation = {'prompt': prompt, 'response': response}

            # 대화 기록에 새로운 응답 추가
            # session_conversations.append(conversation)
            # request.session['conversations'] = session_conversations

            # 대화 기록에 새로운 응답 추가
            session_conversations.append({'prompt': prompt, 'response': response})
            request.session['conversations'] = session_conversations
            request.session.modified = True

            # ChatMessage 모델에 대화 내역 저장
            conversation_content = f"prompt: {prompt} / response: {response}"
            chat_message = ChatMessage(sender=request.user, content=conversation_content)
            chat_message.save()

        return self.get(request, *args, **kwargs)