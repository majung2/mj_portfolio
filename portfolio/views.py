from django.shortcuts import render

# Create your views here.

def home(request): # home.html로 가는 함수
    return render(request, 'portfolio/home.html')

def firstpage(request):
    return render(request, 'portfolio/firstpage.html')

def secondpg(request):
    return render(request, 'portfolio/secondpg.html')

def new(request):
    return render(request, 'portfolio/new.html')

def youtube(request):
    return render(request, 'portfolio/youtube.html')
    
