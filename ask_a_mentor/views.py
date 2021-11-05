from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = { 'posts' : posts }
    return render(request, 'ask_a_mentor_index.html', context)

@login_required(login_url = '/login')
def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ask-a-mentor')

@login_required(login_url = '/login')
def add_comment(request):
    return render(request, 'ask_a_mentor')

def alin(request):
    posts = Post.objects.all()
    context = { 'posts' : posts }
    return render(request, 'alin.html', context)

def mppi(request):
    posts = Post.objects.all()
    context = { 'posts' : posts }
    return render(request, 'mppi.html', context)

def pbp(request):
    posts = Post.objects.all()
    context = { 'posts' : posts }
    return render(request, 'pbp.html', context)

def sda(request):
    posts = Post.objects.all()
    context = { 'posts' : posts }
    return render(request, 'sda.html', context)

def sosi(request):
    posts = Post.objects.all()
    context = { 'posts' : posts }
    return render(request, 'sosi.html', context)

