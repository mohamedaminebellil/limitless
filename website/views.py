from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def signIN(request):
    return render(request, 'SignIn.html')

def register(request):
    return render(request, 'SignUp.html')

def netflix_page(request):
    return render(request, 'netflix.html')

def spotify_page(request):
    return render(request, 'spotify.html')
def about(request):
    return render(request, 'aboutUS.html')