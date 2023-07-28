from django.urls import path
from .views import ChatbotView
from django.views.decorators.csrf import csrf_exempt

app_name = "mychatbot"

urlpatterns = [
	path("", csrf_exempt(ChatbotView.as_view()), name='chat'),
]