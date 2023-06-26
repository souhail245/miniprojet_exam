from django.urls import path
from . import views
from .views import my_template,incendie_foret_detail

urlpatterns = [
    path('', views.my_template, name='my_template'),
    path('incendie/<int:pk>/', views.incendie_foret_detail, name='incendie_foret_detail'),
    path('nouvelle-foret/', views.nouvelle_foret, name='nouvelle_foret'),
    path('nouveau-incendie/', views.nouveau_incendie, name='nouveau_incendie'),
    path('recherche-foret/', views.recherche_foret, name='recherche_foret'),
]
