from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm
# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html')


# def login_page(request):


def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        context = {
            'new_user': new_user
        }
        return render(request, 'user/register_done.html', context)

    return render(request, 'user/register.html', context)

