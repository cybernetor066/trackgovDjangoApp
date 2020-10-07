from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('bills/', views.bills, name='bills'),
]
