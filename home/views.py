from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/dashboard.html')
    # return render(request, 'home/index.html')

def agreements(request):
  return render(request, 'pages/agreements.html')

def acts(request):
  return render(request, 'pages/acts.html')

def reports(request):
  return render(request, 'pages/reports.html')