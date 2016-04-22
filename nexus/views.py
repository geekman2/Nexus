from django.shortcuts import render
from django.utils import timezone
from taggit.managers import TaggableManager
from .models import Post

# Create your views here.
def nexus_home(request):
    stories = Post.objects.filter(type="story").order_by('votes')
    art = Post.objects.filter(type="art").order_by('votes')
    return render(request,'nexus/homepage.html',{'stories':stories,
                                                 'art':art,
                                                 'range':[x for x in range(12)]})