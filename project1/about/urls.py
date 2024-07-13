from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),  # 'about' view fonksiyonu için 
    path('misyon-ve-vizyon/', views.misyon_ve_vizyon, name='misyon-ve-vizyon'),
    path('kalite/', views.kalite, name='kalite'),
   
]

