from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import room
# Create your views here.
@login_required
def roomses(request):
    rooms = room.objects.all()

    return render(request, 'room/index.html', {'rooms': rooms})

@login_required
def room(request, slug):
    rom = room.objects.get(slug=slug)
    
    return render(request, 'room/room.html', {'rom': rom})