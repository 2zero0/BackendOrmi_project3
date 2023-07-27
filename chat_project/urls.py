from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mychatbot', include("mychatbot.urls")),
    path('chatlog', include("chatlog.urls")),
]
