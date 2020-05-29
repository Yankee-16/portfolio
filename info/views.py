from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from info.models import *
from django.db.models import Q, Max
from django.contrib import messages
# from info.forms import Form, UserForm
# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('{} {}'.format(username, password))
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect('user_home')

        else:
            print('Invalid Username or Password!')
            return redirect('home')

    return render(request, 'info/home.html')

def education(request):
    if request.method == "POST":
        user = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect('user_home')

        else:
            messages.error(request, 'Invalid Username or Password!')
            return redirect('education')

    edu = Education.objects.all()
    dict = {'edu':edu}
    return render(request, 'info/education.html', context=dict)

def user_home(request):
    return render(request, 'info/user_home.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
