from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Flower, Garden
from .forms import WateringForm

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
  watering_form = WateringForm()
  return render(request, 'flowers/detail.html', { 
    'flower': flower,
    'watering_form': watering_form, 
  })

def add_feeding(request, flower_id):
  # create a ModelForm instance using the data in request.POST
  form = WateringForm(request.POST)
  if form.is_valid():
    # don't save the form to the db until it has the flower_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.flower_id = flower_id
    new_feeding.save()
  return redirect('detail', flower_id=flower_id)

# @login_required
def assoc_garden(request, flower_id, garden_id):
    Flower.objects.get(id=flower_id).gardens.add(garden_id)
    return redirect('detail', flower_id=flower_id)

# @login_required
def unassoc_garden(request, flower_id, garden_id):
    Flower.objects.get(id=flower_id).gardens.remove(garden_id)
    return redirect('detail', flower_id=flower_id)

class FlowerCreate(CreateView):
  model = Flower
  fields= '__all__'

class FlowerUpdate(UpdateView):
  model = Flower
  fields = ['bloom', 'height', 'spacing', 'hardiness', 'deerResistant', 'pinch', 'image']

class FlowerDelete(DeleteView):
  model = Flower
  success_url = '/flowers'

class GardenCreate(CreateView):
  model = Garden
  fields = ['name', 'color']

class GardenList(ListView):
    model = Garden

class GardenDetail(DetailView):
    model = Garden

class GardenUpdate(UpdateView):
    model = Garden
    fields = ['name', 'color']

class GardenDelete(DeleteView):
    model = Garden
    success_url = '/gardens/'