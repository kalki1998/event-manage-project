from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.contrib import messages
# Create your views here.

def signup(request):
        if request.method == 'POST':
             username = request.POST['username']
             firstname = request.POST['firstname']
             lastname = request.POST['lastname']
             email = request.POST['email']
             password = request.POST['password']
             repassword = request.POST['repassword']
             myuser = User.objects.create_user(username,email,password)
             myuser.f_name = firstname
             myuser.l_name = lastname 
             myuser.save()
             messages.success(request,'your account created successfully.')
             #alert a success message after authentication verified, and save the user details to the database.
             return redirect('login')
        
        return render(request,'log/signup.html')

def login(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']

         user = authenticate(username=username,password=password)

         if user is not None:
              auth_login(request, user)
              f_name = user.first_name
              return render(request,'index.html', {'fname': f_name})

         else:
            messages.error(request, 'bad credentials!')
            return redirect('index')
    return render(request, 'log/signin.html') 
    #authenticate login details and redirect to the index page after verification.if it's an error, it shows alert as 'bad credentials!'.

def logout(request):
    auth_logout(request)
    messages.success(request,'logged out successfully.')
    return redirect('index')
