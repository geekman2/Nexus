from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def nexus_home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'nexus/homepage.html',{'posts':posts,
                                                 'range':[x for x in range(10)]})