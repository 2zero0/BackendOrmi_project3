from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatMessage(models.Model):
    # user모델 만들고 변경 예정
    # sender = models.CharField(max_length=30, null=True, blank=True)

    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()  # prompt와 response 내용을 저장
    timestamp = models.DateTimeField(auto_now_add=True)  # 채팅 메시지 생성 시간 저장

    def __str__(self):
        return f"{self.content}"