from django.shortcuts import render
from django.http import Http404
from django.core import serializers
from django.shortcuts import redirect

from .models import TshirtRoom, Tshirt, Friend

import json

# Create your views here.
def user_root(request):
    if request.method == 'GET':
        tshirts = Tshirt.objects.all()
        return render(request, 'user/create_room.html', {'tshirts': tshirts})
    raise Http404


def register_user(request, tid, name):
    if request.method == 'GET':
        tshirt = Tshirt.objects.get(id=tid)

        tr = TshirtRoom(name = name, tshirt=tshirt)
        tr.save()

        ts_ = serializers.serialize('python', [tshirt])[0]['fields']
        tr_ = serializers.serialize('python', [tr])[0]['fields']

        content = {
            'tshirtroom': tr_,
            'tshirt': ts_,
            'urlinfo': {
                'host': request.get_host(),
                'protocol': request.scheme
            }
        }
        return render(request, 'user/create_room_response.html', content)    
    raise Http404

def register_user_v2(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return ''

def get_room(request, slug):
    if request.method == 'GET':
        tsr = TshirtRoom.objects.get(slug=slug)
        if tsr is None:
            raise Http404
        tsrImg = Tshirt.objects.get(id=tsr.tshirt.id)
        userip = request.META.get("REMOTE_ADDR")
        frd = Friend(name="", tshirt_room=tsr, key_points="[]", ip=userip)
        frd.save()

        frds = Friend.objects.filter(tshirt_room=tsr).values()
        
        tsr = serializers.serialize('python', [tsr])[0]
        frds = list(frds)
        frdd = serializers.serialize('python', [frd])[0]
        frdd['id'] = frd.id

        print("==>", tsr, frds, frdd)

        return render(request, 'user/room2.html', {'tsr': tsr, 'frds': frds, "frd": frdd , 'host': request.get_host(), 'tsrImg': tsrImg})

'''
Get user's ip
request.META.get("REMOTE_ADDR")
'''