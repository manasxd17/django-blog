from django.shortcuts import render, HttpResponseRedirect
from .forms import Signup,login_user,User, add_blog
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import blog_post


def index(request):
    posts = blog_post.objects.all()
    return render(request,'blog/index.html',{'posts':posts})

def dashboard(request):
    if request.user.is_authenticated:
        posts = blog_post.objects.all()
        return render(request, 'blog/dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect(request, '/login/')
    

def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = login_user(request=request, data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    auth_login(request,user)
                    messages.success(request,'Logged in successfully!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = login_user()
            return render(request, 'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


def signup(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            messages.success(request,"YOU'VE AUTHOR RIGHTS NOW!")
            form.save()
    else:
        form = Signup()
    return render(request, 'blog/signup.html',{'form':form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def table(request):
    authors = User.objects.all()
    return render(request, 'blog/table.html',{'authors':authors})


def add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = add_blog(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = blog_post(title = title, desc = desc)
                pst.save()
                form = add_blog()
        else:
            form = add_blog()
        return render(request, 'blog/add.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def update(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bid = blog_post.objects.get(pk = id)
            form = add_blog(request.POST, instance=bid)
            if form.is_valid():
                form.save()
                form = add_blog()
        else:
            bid = blog_post.objects.get(pk = id)
            form = add_blog(instance=bid)
        return render(request, 'blog/update.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bid = blog_post.objects.get(pk = id)
            bid.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
