from django.urls import path
from . import views

app_name = 'chatlog'

urlpatterns = [
	# 채팅 내역 조회
  path("", views.Index.as_view(), name='list'), 
]