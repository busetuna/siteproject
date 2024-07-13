from django.urls import include, path
from . import views

urlpatterns = [
    path("" , views.index),
    path("references/", views.references , name ='references'),
    path("contact/", views.contact , name ='contact'),
    path("language/", views.language , name = 'language'),
    path('about/' , views.about , name= 'about'),
    path('kalite', views.kalite , name='kalite'),
    path('misyon-ve-vizyon/', views.misyon_ve_vizyon  , name='misyon-ve-vizyon'),
]
