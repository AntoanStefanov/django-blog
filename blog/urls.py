from django.urls import path
from . import views

urlpatterns = [
    # views.home handles this path (route) ''
    path('', views.home, name='blog_home'),
    # views.about handles this path (route) 'about/'
    path('about/', views.about, name='blog_about'), 
]
