from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

### User's chatlog List
class Index(APIView):
    # 로그인이 필요한 데코레이터 추가
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(Index, self).dispatch(*args, **kwargs)
    
    def get(self, request):
        chatmsgs = ChatMessage.objects.filter(sender=request.user).order_by('-timestamp')
        serialized_chatmsgs = ChatMessageSerializer(chatmsgs, many=True)
        return Response(serialized_chatmsgs.data)