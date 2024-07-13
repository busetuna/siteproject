from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def references(request):
    return render(request, 'references.html')

def contact(request):
    return render(request, 'contact.html')

def language(request):
    return render(request, 'language.html')

def about(request):
    return render(request, 'about.html')

def kalite(request):
    return render(request, 'kalite.html')

def misyon_ve_vizyon(request):
    return render(request, 'misyon_ve_vizyon.html')
