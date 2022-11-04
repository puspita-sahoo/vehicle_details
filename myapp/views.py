from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import SuperUser, User, vehicle
from django.contrib.messages import error, success
from django.contrib.auth import logout, login
from django.contrib import auth



def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        username = request.POST.get('username')
        if request.POST.get('password') == request.POST.get('cpassword'):
            try:
                user = SuperUser.objects.get(username=username)
                error(request, 'UserName Already Exist')
                return render(request, 'signup.html')
            except SuperUser.DoesNotExist:
                user = SuperUser(full_name=full_name, username=username,
                                 password=request.POST.get('password'))
                user.save()
                success(request, 'Your Registration successfull ! Please Login')
                return redirect('/')
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = SuperUser.objects.filter(
            username=username, password=password)
        if user_obj:
            request.session['username'] = username
            return redirect('myapp/home/')
        else:
            error(request, 'invalid username or Password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def home(request):
    all_obj = vehicle.objects.all()
    return render(request, 'home.html', {"data": all_obj})
