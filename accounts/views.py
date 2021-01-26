from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from educator.models import Educator
from manager.models import Manager
from base.decorators import reverse


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        print("hello")
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='educator')
            user.groups.add(group)
            Educator.objects.create(
                user=user,
                nick_name=user.username,
                email=user.email,
                )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        
    context = {'form':form}
    return render(request, 'register.html', context)



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@reverse
def profile(request):
    user = request.user
    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
    if group == 'educator':
        person = request.user.educator
    if group == 'manager':
        person = request.user.manager
    if group == 'human':
        person = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form':form, 'person':person}
    return render(request, 'profile.html', context)




def updateEducator(request, pk):
    user = request.user
    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
    if group == 'educator':
        person = request.user.educator
    if group == 'manager':
        person = request.user.manager
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form':form, 'person':person}
    return render(request, 'profile.html', context)
