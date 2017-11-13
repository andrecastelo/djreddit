from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views import View

from core.forms import LoginForm

class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                return self.login_and_redirect(request, user)

        messages.error(request, "The username and password were incorrect.")
        return HttpResponseRedirect(reverse_lazy('login'))

    def login_and_redirect(request, user):
        login(request, user)
        messages.success(request, 'You are now logged in.')
        return HttpResponseRedirect('/')