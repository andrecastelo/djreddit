from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from core.forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        return do_login(request)
    else:
        return render(request, 'login.html', {'form': LoginForm()})


def do_login(request):
    form = LoginForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            return login_and_redirect(request, user)

    messages.error(request, "The username and password were incorrect.")
    return HttpResponseRedirect(reverse('login'))


def login_and_redirect(request, user):
    login(request, user)
    messages.success(request, 'You are now logged in.')
    return HttpResponseRedirect('/')