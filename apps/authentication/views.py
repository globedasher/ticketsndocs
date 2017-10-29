from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
import bcrypt

from .models import User

def index(request):
    try:
        all_users = User.objects.all()
        context = { 'all_users': all_users }
        return render(request, 'log_n_reg_app/index.html', context)
    except:
        return render(request, 'log_n_reg_app/index.html')

def home(request):
    if not 'id' in request.session:
        messages.error(request, "Please login first.")
        return redirect(reverse('login:index'))
    if request.session['id']:
        all_users = User.objects.all()
        context = { 'all_users': all_users }
        return render(request, "log_n_reg_app/home.html", context)

""" 
The tuple_return in the login and register functions return a true if the email
is cleared by regex match and and User object. If the email is not cleared by
regex, the tuple comes back as false at [0] and an error message at [1].
"""

def login(request):
    if request.method == 'POST':
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

def logout(request):
    del request.session['id']
    del request.session['email']
    return redirect(reverse('login:index'))


def register(request):
    if request.method == 'POST':
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

