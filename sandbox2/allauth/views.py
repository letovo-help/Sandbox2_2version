from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import createUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

"""from .forms import *
import account.forms
import account.views"""

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('all requests')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('all requests')
            else:
                messages.error(request, 'Неверная почта или пароль')
                return render(request, 'accounts/login.html')
        return render(request, 'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login page')

def register(request):
    if request.user.is_authenticated:
        return redirect('all requests')
    else:
        form = createUserForm()
        if request.method == "POST":
            form = createUserForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)

"""class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm

class SignupView(account.views.SignupView):
    print(2)
    form_class = SignupForm

    def generate_username(self, form):
        username = form.cleaned_data["email"]
        return username

    def after_signup(self, form):
        # do something
        super(SignupView, self).after_signup(form)"""
