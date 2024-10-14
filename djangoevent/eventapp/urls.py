from django.urls import path,include
from eventapp import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('events/', views.events, name='events'),
]