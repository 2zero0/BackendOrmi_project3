from django.urls import path
from .views import ChatbotView

app_name = "mychatbot"

urlpatterns = [
	path("", ChatbotView.as_view(), name='chat'),
]