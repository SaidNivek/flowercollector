from django.shortcuts import render

# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def flowers_index(request):
  return render(request, 'flowers/index.html', {
    'flowers': flowers
  })

# views.py

# Add this cats list below the imports
flowers = [
    {
        'name': 'Chat Noir', 
        'type': 'Dahlia', 
        'description': 'With a superb vase life, spectacular rich deep red flowers resembling sea urchins with their elongated velvety petals, Dahlia "Chat Noir" is acclaimed by many garden enthusiasts. Why? Just look at it. The fully double flowers, up to 6-8 in. wide (15-20 cm), are not top-heavy because they contain little water. They stand nice and straight even when it rains.', 
        'image': 'https://www.gardenia.net/storage/app/public/uploads/images/detail/202541.webp',
        'deerResistant': False
    },   
    {
        'name': 'Hot Lips', 
        'type': 'Salvia', 
        'description': "Salvia microphylla 'Hot Lips' (Littleaf Sage) blooms all summer with eye-catching red and white bicolor flowers. The nectar-rich flowers attract hummingbirds and other pollinators.", 
        'image': 'https://www.highcountrygardens.com/media/catalog/product/s/a/salvia_microphylla_hot_lips_close_up_of_flwrs_cc.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=560&width=560&canvas=560:560',
        'deerResistant': True
    },
]
