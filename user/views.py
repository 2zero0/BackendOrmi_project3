from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import RegisterForm, LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import User

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
            return redirect('user:login')
        
        context = {
            'form': form
        }
        return render(request, 'user/user_register.html', context)

### Login
class Login(View):
    def get(self, request):
        # if request.user.is_authenticated:
        #     return redirect('mychatbot:chat')
        
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
    

### JWT
### Register
class RegistrationAPIView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        nickname = request.data.get("nickname")

        if User.objects.filter(username=username).exists():
            message = "User already exists."
            status_code = status.HTTP_400_BAD_REQUEST
        else:
            user = User.objects.create_user(username=username, password=password,  nickname = nickname)
            user.save()
            message = "Registration successful."
            status_code = status.HTTP_201_CREATED
        
        return Response({"message": message}, status=status_code)
