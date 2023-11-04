from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic
from .forms import RoomForm
from django.http import HttpResponse


# rooms = [
#     {'id': 1, 'name': "Lets learn python"},
#     {'id': 2, 'name': "desgin with me"},
#     {'id': 3, 'name': "front end devs"},
# ]

def loginpage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user=user)
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist")

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutuser(request):
    logout(request) 
    return redirect('home')

def registerpage(request):

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occured during registration")

    context = {
        'form': form
    }

    return render(request, 'base/login_register.html', context)


def home(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()

    room_count = rooms.count()

    context = {
        "rooms": rooms,
        "topics": topics,
        "room_count": room_count
    }

    return render(request, 'base/home.html', context)

def room(request, pk):
    
    room = Room.objects.get(id=pk)

    context = {'room': room}

    return render(request, 'base/room.html', context)

@login_required(login_url='/login')
def createroom(request):

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoomForm()

    context = {'form': form}

    return render(request, 'base/room_form.html', context)


@login_required(login_url='/login')
def updateroom(request, pk):
   
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("Your are not allowed here")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'base/room_form.html', context)


@login_required(login_url='/login')
def deleteroom(request, pk):
    
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("Your are not allowed here")
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {'obj': room}
    return render(request, 'base/delete.html', context)







