from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import RegisterForm, LoginForm

### Registration
class Registration(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'user/user_register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('mychatbot:chat')
        
        context = {
            'form': form
        }
        return render(request, 'user/user_register.html', context)

### Login
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('mychatbot:chat')
        
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'user/user_login.html', context)
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('mychatbot:chat')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password) 
            
            if user:
                login(request, user)
                return redirect('mychatbot:chat')
            
        form.add_error(None, '아이디가 없습니다.')
        context = {
            'form': form
        }
        return render(request, 'user/user_login.html', context)


### Logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('mychatbot:chat')