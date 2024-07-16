from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render

from .models import Room

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    # room = Room.objects.get(slug=slug)
    # return render(request, 'room/room.html', {'room', room})
    room = get_object_or_404(Room, slug=slug)
    context = {'room': room}
    print(context)
    return render(request, 'room/room.html', context)
