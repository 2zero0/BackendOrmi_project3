from django.db import models

class ChatMessage(models.Model):
    sender = models.CharField(max_length=30, null=True, blank=True)
    content = models.TextField()  # prompt와 response 내용을 저장
    timestamp = models.DateTimeField(auto_now_add=True)  # 채팅 메시지 생성 시간 저장

    def __str__(self):
        return f"{self.content}"