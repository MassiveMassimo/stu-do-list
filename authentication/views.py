from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def sign_in(request):
    return HttpResponse("Sign in page")