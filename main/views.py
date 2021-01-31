# Create your views here.
from django.shortcuts import render


def main(request):
    context={'like':'Django 很棒'}
   
    
    return render(request, 'main/main.html',context)