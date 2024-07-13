from django.shortcuts import render

def about(request):
    return render(request, 'about/about.html')
  
def misyon_ve_vizyon(request):
    return render(request, 'about/misyon_ve_vizyon.html')

def kalite(request):
    return render(request, 'about/kalite.html')


