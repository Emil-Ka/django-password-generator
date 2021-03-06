from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html', {'password': 'qwerty'})

def password(request):
    characters = list('abcdefghijlkmnopqrstuvwxyz')

    newpassword = ''

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
      characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
      characters.extend(list('0123456789'))
    if request.GET.get('specials'):
      characters.extend(list('!@#$%^&*?'))

    for i in range(length):
      newpassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password': newpassword})

def about(request):
  return render(request, 'generator/about.html')