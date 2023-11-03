from django.shortcuts import render
from .models import Room

rooms = [
    {'id': 1, 'name': "Lets learn python"},
    {'id': 2, 'name': "desgin with me"},
    {'id': 3, 'name': "front end devs"},
]

def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):

    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}

    return render(request, 'base/room.html', context)
