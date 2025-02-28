from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def home(request):
    fullname = None
    pic = None
    usernameofuser = None
    email = None
    if request.user.is_authenticated:
        username = request.user.username
        user = profileInformations.objects.filter(username = username).first()
        if user:
            usernameofuser = user.username
            fullname = user.fname.capitalize() + " " + user.lname.capitalize()
            pic = user.profilePic
            email = user.email
    posts = userPost.objects.all()
    context = {
        'username':usernameofuser,
        'name':fullname,
        'pic':pic,
        'email': email,
        'posts':posts,
    }
    return render(request, 'home.html', context)


def profile(request):
    fullname = None
    pic = None
    usernameofuser = None
    email = None
    if request.user.is_authenticated:
        username = request.user.username
        user = profileInformations.objects.filter(username = username).first()
        if user:
            usernameofuser = user.username
            fullname = user.fname.capitalize() + " " + user.lname.capitalize()
            pic = user.profilePic
            email = user.email
    posts = userPost.objects.filter(theUser = usernameofuser)


    context = {
        'username':usernameofuser,
        'name':fullname,
        'pic':pic,
        'email': email,
        'posts': posts,
    }
    return render(request, 'profile.html', context)



def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')

        if User.objects.filter(username = username).exists():
            user = authenticate(request, username = username,password = password)
            if user :
                login(request, user)
                messages.success(request, "Login succesfull")
                return redirect('home')
            else :
                messages.error(request, "worng passowrd")
        else :
            messages.error(request, "user doesn't exist")
    return render(request, 'login.html' )

def sign_up(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        pic = request.FILES.get('profilepic')

        if pass1 != pass2:
            messages.error(request, "Unmatched password")
            return redirect('signup')
        if User.objects.filter(username = username).exists():
            messages.error(request, "this username exist ")
            return redirect('signup')
        user = User.objects.create_user(username=username, email=email, password=pass1)
        user.save()
        login(request, user)

        profileInformations.objects.create(
            fname = fname, 
            lname = lname, 
            username = username, 
            email = email, 
            password = pass1, 
            profilePic = pic)
        
        return redirect('home')
    return render(request, 'signup.html' )


# checkign user name is availble or not 
from django.http import JsonResponse

def check_username(request):
    if request.method == "GET":
        username = request.GET.get('username', None)  # Get username from request
        if username and User.objects.filter(username=username).exists():
            return JsonResponse({'available': False, 'message': 'Username is already taken!'})
        return JsonResponse({'available': True, 'message': 'Username is available!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def log_out(request):
    logout(request)
    messages.success(request, "Logout successfull")
    return redirect('home')




def createPost(request):
    print(request.user)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        username = request.user.username
        # print(username)
        if title and description:
            userPost.objects.create(theUser = username, title = title, description = description)
            return redirect('home')
        redirect('createPost')
    return render(request, 'createPost.html')