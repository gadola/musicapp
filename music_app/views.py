from django.shortcuts import render
from django.views import View
from .models import Song,PlayList
# Create your views here.


def index(request):
    return render(request,'music_app/index.html')


class MusicView(View):
    
    def get(self,request):
        songs = Song.objects.all()
        
        context = {
           'songs':songs,
           
        }
        return render(request,'music_app/index.html',context)
    
