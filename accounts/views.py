from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .jwt_utils import create_token


# def login_view(request):
#     form = AuthenticationForm()
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect('home')
#         else:
#             form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})


# def signup_view(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#         else:
#             form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token = create_token(user.id, user.username)
            response = redirect('home') 
            response.set_cookie('token', token) 
            return response
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm()
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            token = create_token(user.id, user.username)
            response = redirect('home')
            response.set_cookie('token', token)
            return response        
        else:
            messages.error(request, form.errors.as_text())
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('home')
