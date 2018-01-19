from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import bcrypt

from django.contrib.auth.models import User

#from .models import User

def index(request):
    try:
        all_users = User.objects.all()
        context = { 'all_users': all_users }
        return render(request, 'authentication/index.html', context)
    except:
        return render(request, 'authentication/index.html')

def home(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login first.")
        return redirect(reverse('login:index'))
    return render(request, "authentication/home.html")

def users(request):
    print(request)
    if not request.user.is_authenticated:
        messages.error(request, "Please login first.")
        return redirect(reverse('login:index'))
    all_users = User.objects.all()
    context = { 'all_users': all_users }
    return render(request, "authentication/users.html", context)

"""
The tuple_return in the login and register functions return a true if the email
is cleared by regex match and and User object. If the email is not cleared by
regex, the tuple comes back as false at [0] and an error message at [1].
"""

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successful login!")
            return redirect(reverse('login:home'))
        else:
            messages.error(request, "Login errors")
            return redirect(reverse('login:index'))
    else:
        messages.error(request, "Incorrect Http request.")
        return redirect(reverse('login:index'))



def logout_view(request):
    #del request.session['id']
    #del request.session['email']
    logout(request)
    return redirect(reverse('login:index'))


#TODO: I need to build registration validation of form data...
def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(
                   request.POST['username'],
                   request.POST['email'],
                   request.POST['password'],
               )
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        login(request, user)
        messages.success(request, "Successful registration!")
        return redirect(reverse('login:home'))
    else:
        messages.error(request, "Incorrect Http request.")
        return redirect(reverse('login:index'))

