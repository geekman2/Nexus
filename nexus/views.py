from django.shortcuts import render

# Create your views here.
def nexus_home(request):
    return render(request,'nexus/homepage.html',{})