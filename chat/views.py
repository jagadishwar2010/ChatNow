from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse


# Create your views here.
def front_page(request):
    return render(request, 'chat/front_page.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('front_page')
        else:
            # handle form validation errors
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label} : {error}")

    else:
        form = SignUpForm

    return render(request, 'chat/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('front_page')
        else:
            messages.error(request, 'Username or password is incorrect')
    else:
        form = LoginForm
    return render(request, 'chat/login.html', {'form': form})
