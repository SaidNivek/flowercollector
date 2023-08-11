from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('flowers/', views.flowers_index, name='index'),
    path('flowers/<int:flower_id>/', views.flowers_detail, name='detail'),
    path('flowers/create/', views.FlowerCreate.as_view(), name='flowers_create'),
    path('flowers/<int:pk>/update/', views.FlowerUpdate.as_view(), name='flowers_update'),
    path('flowers/<int:pk>/delete/', views.FlowerDelete.as_view(), name='flowers_delete'),
    path('flowers/<int:flower_id>/add_watering/', views.add_watering, name='add_watering'),
    path('gardens/', views.GardenList.as_view(), name='gardens_list'),
    path('gardens/<int:pk>/', views.GardenDetail.as_view(), name='gardens_detail'),
    path('gardens/create/', views.GardenCreate.as_view(), name='gardens_create'),
    path('gardens/<int:pk>/update/', views.GardenUpdate.as_view(), name='gardens_update'),
    path('gardens/<int:pk>/delete/', views.GardenDelete.as_view(), name='gardens_delete'),
    path('cats/<int:flower_id>/add_watering/', views.add_watering, name='add_watering'),
    path('cats/<int:flower_id>/assoc_garden/<int:garden_id>/', views.assoc_garden, name='assoc_garden'),
    path('cats/<int:flower_id>/unassoc_garden/<int:garden_id>/', views.unassoc_garden, name='unassoc_garden'),
    path('accounts/signup/', views.signup, name='signup'),
    path('flowers/<int:flower_id>/add_photo/', views.add_photo, name='add_photo')
]
