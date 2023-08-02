from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('flowers/', views.flowers_index, name='about'),
    path('flowers/<int:flower_id>/', views.flowers_detail, name='detail')
]
