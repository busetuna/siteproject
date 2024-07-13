from django.shortcuts import render

def about(request):
    return render(request, 'about/about.html')  # 'about/about.html' şablon dosyasını render edin

def kalite(request):
    return render(request, 'about/kalite.html')

def misyon_ve_vizyon(request):
    return render(request, 'about/misyon_ve_vizyon.html')
