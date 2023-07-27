from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatMessage
from .serializers import ChatMessageSerializer

# Create your views here.
### List
class Index(APIView):
    
    def get(self, request):
        chatmsgs = ChatMessage.objects.all()
        serialized_chatmsgs = ChatMessageSerializer(chatmsgs, many=True)# 직렬화
        return Response(serialized_chatmsgs.data)