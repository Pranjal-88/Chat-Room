from django.shortcuts import render,redirect
from .models import Room,Message
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    if request.method=="POST":
        unm=request.POST["username"]
        room_name=request.POST["roomid"]
        if Room.objects.filter(name=room_name).exists():
            return redirect(f"room={room_name}/user={unm}")
        else:
            new_room=Room.objects.create(name=room_name)
            new_room.save()
            return redirect(f"room={room_name}/user={unm}")
    return render(request,"index.html")


def room(request,name,username):
    if request.method=="POST":
        message=request.POST["message"]
        new_obj=Message.objects.create(content=message,user=username,room_id=name,time=datetime.now().time())
        new_obj.save()
        return redirect(reverse('room', args=(name, username)))
    
    all_messages=Message.objects.filter(room_id=name)
    return render(request,"room.html",{'name':name,'username':username.capitalize(),'messages':all_messages})
