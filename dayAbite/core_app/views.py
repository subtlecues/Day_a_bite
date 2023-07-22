from django.http import HttpResponse
from django.shortcuts import render, redirect
from custom_user.models import User
from django.contrib.auth import authenticate, login, logout






def index(request):

    return render(request, 'hello.html', )

def registration_handler(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth
        )

        user.save()

    return render(request, 'register_user.html')



def login_handler(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            return render(request, 'login.html', {'error': 'Wrong username or password'})

    # If it's a GET request, show the login form
    return render(request, 'login.html')
def logout_handler(request):
    logout(request)
    return render(request, 'hello.html')