from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'media/home.html')


def profile(request):
    return render(request, 'media/profile.html')
