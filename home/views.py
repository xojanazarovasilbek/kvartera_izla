from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def aloqa(request):
    return render(request, 'boglanish.html')
# Create your views here.
