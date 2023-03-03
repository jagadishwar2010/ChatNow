from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
# Create your views here.


@login_required
def rooms(request):
    all_rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': all_rooms})


@login_required
def room(request, slug):
    join_room = Room.objects.get(slug=slug)

    return render(request, 'room/room.html', {'room': join_room})