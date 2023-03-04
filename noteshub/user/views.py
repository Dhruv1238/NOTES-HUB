from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from social_django.utils import psa
# from allauth.socialaccount.decorators import *

# Create your views here.
# @login_required
def home(request):
    return render(request, 'user/login.html')



@psa('social:complete', 'google-oauth2')
def google_auth(request, backend):
    return redirect('/')

@psa('social:complete', 'google-oauth2')
def google_auth_done(request, *args, **kwargs):
    return redirect('/')