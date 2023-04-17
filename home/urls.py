from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agreements/',  views.agreements,  name='agreements' ),
    path('acts/',  views.acts,  name='acts' ),
    path('reports/',  views.reports,  name='reports' ),
    path('schemes/',  views.schemes,  name='schemes' ),
    path('guides/',  views.guides,  name='guides' ),
    path('accounting_tables/',  views.accounting_tables,  name='accounting_tables' ),
    path('accounting/<int:pk>/', views.AccountingDetailView.as_view(), name='accounting_detail'),
]
