from django.urls import include, path
from . import views

urlpatterns = [
    path("" , views.index , name="index"),
    path("index/", views.index ,name="index"),
    path("hizmetler/", views.hizmetler , name="hizmetler"),
    path("references/", views.references , name ='references'),
   
    path("language/", views.language , name = 'language'),
   path('urunler/', views.urunler , name="urunler"),
]
