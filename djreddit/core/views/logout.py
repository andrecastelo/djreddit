from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.success(request, "You are logged out.")
    return HttpResponseRedirect(reverse_lazy('index'))
