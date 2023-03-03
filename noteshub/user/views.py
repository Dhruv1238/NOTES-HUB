from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from social_django.utils import psa
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required
def home(request):
    return render(request, 'user/login.html')

@psa('social:complete')
@csrf_exempt
def google_auth(request, backend):
    return do_auth(request.backend, redirect_name='home')

def do_auth(backend, redirect_name):

    return HttpResponse("Authentication failed")