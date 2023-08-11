import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Flower, Garden, Photo
from .forms import WateringForm


# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def flowers_index(request):
  flowers = Flower.objects.filter(user=request.user)
  return render(request, 'flowers/index.html', {
    'flowers': flowers
  })

@login_required
def flowers_detail(request, flower_id):
  flower = Flower.objects.get(id=flower_id)
  # Get gardens the flower is not currently in
  gardens_flower_not_in = Garden.objects.exclude(id__in = flower.gardens.all().values_list('id'))
  watering_form = WateringForm()
  return render(request, 'flowers/detail.html', { 
    'flower': flower,
    'watering_form': watering_form,
    'gardens': gardens_flower_not_in, 
  })

@login_required
def add_watering(request, flower_id):
  # create a ModelForm instance using the data in request.POST
  form = WateringForm(request.POST)
  if form.is_valid():
    # don't save the form to the db until it has the flower_id assigned
    new_watering = form.save(commit=False)
    new_watering.flower_id = flower_id
    new_watering.save()
  return redirect('detail', flower_id=flower_id)

@login_required
def assoc_garden(request, flower_id, garden_id):
    Flower.objects.get(id=flower_id).gardens.add(garden_id)
    return redirect('detail', flower_id=flower_id)

@login_required
def unassoc_garden(request, flower_id, garden_id):
    Flower.objects.get(id=flower_id).gardens.remove(garden_id)
    return redirect('detail', flower_id=flower_id)

class FlowerCreate(LoginRequiredMixin, CreateView):
  model = Flower
  fields= ['name', 'plantType', 'bloom', 'height', 'spacing', 'hardiness', 'pinch', 'deerResistant']

  # This inherited method is called when a
  # valid flower form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class FlowerUpdate(LoginRequiredMixin, UpdateView):
  model = Flower
  fields = ['bloom', 'height', 'spacing', 'hardiness', 'deerResistant', 'pinch']

class FlowerDelete(LoginRequiredMixin, DeleteView):
  model = Flower
  success_url = '/flowers'

class GardenCreate(LoginRequiredMixin, CreateView):
  model = Garden
  fields = ['name', 'length', 'width']

class GardenList(LoginRequiredMixin, ListView):
    model = Garden

class GardenDetail(LoginRequiredMixin, DetailView):
    model = Garden

class GardenUpdate(LoginRequiredMixin, UpdateView):
    model = Garden
    fields = ['name', 'length', 'width']

class GardenDelete(LoginRequiredMixin, DeleteView):
    model = Garden
    success_url = '/gardens/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def add_photo(request, flower_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to flower_id or flower (if you have a flower object)
            Photo.objects.create(url=url, flower_id=flower_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', flower_id=flower_id)