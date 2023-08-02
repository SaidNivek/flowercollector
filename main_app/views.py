from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Flower

# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def flowers_index(request):
  flowers = Flower.objects.all()
  return render(request, 'flowers/index.html', {
    'flowers': flowers
  })

def flowers_detail(request, flower_id):
  flower = Flower.objects.get(id=flower_id)
  return render(request, 'flowers/detail.html', { 'flower': flower })

class FlowerCreate(CreateView):
  model = Flower
  fields= '__all__'
