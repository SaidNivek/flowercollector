from django.shortcuts import render
from .models import Flower

# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def flowers_index(request):
  flowers = Flower.objects.all()
  return render(request, 'flowers/index.html', {
    'flowers': flowers
  })

# main_app/views.py

...

def flowers_detail(request, flower_id):
  flower = Flower.objects.get(id=flower_id)
  return render(request, 'flowers/detail.html', { 'flower': flower })

