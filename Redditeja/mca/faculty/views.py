from django.shortcuts import render

# Create your views here.
def Reddy(request):
    return render(request, 'Reddy.html')
def Teja(request):
    return render(request, 'Teja.html')
def First(request):
    return render(request, 'First.html')
def home(request):
    return render(request, 'home.html')
