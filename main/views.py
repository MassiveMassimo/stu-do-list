from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login as auth_login, login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'main/home.html')

def register_req(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

def login_req(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context = {"login_form":form})

@csrf_exempt
def login_flutter(request):
    _username = request.POST.get('username')
    _password = request.POST.get('password')
    user = authenticate(username=_username, password=_password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            redirect("main:home")
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!"
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)
    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)

@login_required(login_url = '/login')
def logout_req(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:home")

