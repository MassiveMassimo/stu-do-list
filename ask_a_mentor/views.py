from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ask_a_mentor_index.html')