from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
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
