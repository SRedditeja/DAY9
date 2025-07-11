from django.shortcuts import render

# Create your views here.
def red(request):
    return render(request, 'red.html')
def skyblue(request):
    return render(request, 'skyblue.html')
def pink(request):
    return render(request, 'pink.html')
