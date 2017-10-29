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
        return render(request, 'log_n_reg_app/index.html', context)
    except:
        return render(request, 'log_n_reg_app/index.html')

def home(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login first.")
        return redirect(reverse('login:index'))
    return render(request, "log_n_reg_app/home.html")

def users(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login first.")
        return redirect(reverse('login:index'))
    all_users = User.objects.all()
    context = { 'all_users': all_users }
    return render(request, "log_n_reg_app/users.html", context)

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




        tuple_return = User.objects.login(request.POST['email'], 
                request.POST['password'])
        # tuple_return[0] is false if email didn't pass regex
        if tuple_return[0] == False:
            messages.error(request, "Login errors:")
            # Here, tuple_retun[1] is a list of error messages to flash to user
            for item in tuple_return[1]:
                messages.error(request, item)
            return redirect(reverse('login:index'))
        # tuple_return[0] is false if email didn't pass regex
        elif tuple_return[0] == True:
            request.session['id'] = tuple_return[1].id
            request.session['email'] = tuple_return[1].email
            messages.success(request, "Successful login!")
            return redirect(reverse('login:home'))
    else:
        messages.error(request, "Incorrect Http request.")
        return redirect(reverse('login:index'))

def logout_view(request):
    #del request.session['id']
    #del request.session['email']
    logout(request)
    return redirect(reverse('login:index'))


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



        tuple_return = User.objects.register(request.POST)
        # tuple_return[0] is false if email didn't pass regex
        if tuple_return[0] == False:
            messages.error(request, "Registration errors:")
            # Here, tuple_retun[1] is a list of error messages to flash to user
            for item in tuple_return[1]:
                messages.error(request, item)
            return redirect(reverse('login:index'))
        # tuple_return[0] is false if email didn't pass regex
        elif tuple_return[0] == True:
            request.session['id'] = tuple_return[1].id
            request.session['email'] = tuple_return[1].email
            messages.success(request, "Successful registration!")
            return redirect(reverse('login:home'))
    else:
        messages.error(request, "Incorrect Http request.")
        return redirect(reverse('login:index'))

