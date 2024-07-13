from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),  # 'about' view fonksiyonu için
    path('about/kalite/', views.kalite, name='kalite'),
    path('about/misyon-ve-vizyon/', views.misyon_ve_vizyon, name='misyon-ve-vizyon'),
]

