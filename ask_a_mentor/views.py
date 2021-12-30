from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Post, Comment
from .forms import PostForm, CommentForm
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = { 'posts' : posts }
    return render(request, 'ask_a_mentor_index.html', context)

@login_required(login_url = '/login')
def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    
    if (form.is_valid() and request.method == 'POST'):
        profile = form.save(commit=False)
        profile.user = request.user
        form.save()
        return HttpResponseRedirect('/ask-a-mentor')
    
    context = {'form' : form }
    return render(request, 'add_post.html', context)

@login_required(login_url = '/login')
def lihat_post(request, id):
    post = Post.objects.get(id=id)
    komen = Comment.objects.all()
    context = { 'post' : post, "komen" : komen }
    return render(request, 'post.html', context)
    

@login_required(login_url = '/login')
def add_comment(request, id):
    form = CommentForm(request.POST or None, request.FILES or None)
    if (form.is_valid() and request.method == 'POST'):
        profile = form.save(commit=False)
        profile.user = request.user
        form.save()
        return HttpResponseRedirect('/ask-a-mentor')
    
    context = {'form' : form }
    return render(request, 'add_komen.html', context)

class post_json(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class comment_json(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

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

