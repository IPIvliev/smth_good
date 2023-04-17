from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView 
from .models import Agreement, Guide, AccountingTable

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/dashboard.html')
    # return render(request, 'home/index.html')

def agreements(request):
  agreements = Agreement.objects.all()
  return render(request, 'pages/agreements.html', {
    'agreements': agreements,
  })

def acts(request):
  return render(request, 'pages/acts.html')

def reports(request):
  return render(request, 'pages/reports.html')

def schemes(request):
  return render(request, 'pages/scheme.html')

def guides(request):
  guides = Guide.objects.all()
  return render(request, 'pages/guides.html', {
    'guides': guides,
  })

def accounting_tables(request):
  accounting_tables = AccountingTable.objects.all()
  return render(request, 'pages/accounting_tables.html', {
    'accounting_tables': accounting_tables,
  })

# def accounting_page(request):
#   accounting_tables = AccountingTable.objects.all()
#   return render(request, 'pages/accounting_tables.html', {
#     'accounting_tables': accounting_tables,
#   })

class AccountingDetailView(DetailView): # новое
    model = AccountingTable
    template_name = 'pages/accounting_page.html'