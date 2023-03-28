from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agreements/',  views.agreements,  name='agreements' ),
    path('acts/',  views.acts,  name='acts' ),
    path('reports/',  views.reports,  name='reports' ),
]
