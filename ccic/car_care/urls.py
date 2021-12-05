
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='care_care'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('services/', views.services, name='Services'),
    path('booking/', views.booking, name='booking'),
    path('gallery/', views.gallery, name='gallery'),


]
