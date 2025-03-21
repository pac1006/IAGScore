'''
This file contains the views for the accounts app.
'''
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def custom_login(request):
    '''
    This view is used to log in the user.
    '''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('profile')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def profile(request):
    '''
    This view is used to display the user profile.
    '''
    return render(request, 'accounts/profile.html')


def register(request):
    '''
    This view is used to register a new user.
    '''
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Usuario creado correctamente')
            return redirect('login')

        messages.add_message(request, messages.ERROR,
                            user_form.errors.as_text())
    else:
        user_form = RegisterForm()

    return render(request, 'accounts/register.html', {'user_form': user_form})
