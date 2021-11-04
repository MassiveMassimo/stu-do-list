from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ask_a_mentor_index.html')

@login_required(login_url = '/login')
def profile(request):
    return render(request, 'ask_a_mentor')