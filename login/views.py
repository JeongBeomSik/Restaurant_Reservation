from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')    

def create(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST["username"]
            password = request.POST["password1"]
            email = request.POST["email"]
            address = request.POST["address"]
            phone = request.POST["phone"]
            birth = request.POST["birth"]
            user = User.objects.create_user(username, email, password)
            user.address = address
            user.phone = phone
            user.birth = birth
            user.save()
            auth.login(request, user)  
            return redirect('login')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('base')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')    

def logout(request):
    auth.logout(request)
    return redirect('base')

                 