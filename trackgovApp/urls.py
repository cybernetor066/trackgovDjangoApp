from django.urls import path, include

from . import views

# app_name = 'trackgovApp'

urlpatterns = [
    path('', views.index, name='index'),
    path(r'comments/', include('django_comments_xtd.urls')),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('recoverpw/', views.recoverpw, name='recoverpw'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('dashboardstarter/', views.dashboard_starter, name='dashboardstarter'),
    path('dashboardbillprogress/', views.dashboard_bill_progress, name='dashboardbillprogress'),


    path('categories/', views.categories, name='categories'),
    path('bills/', views.bills, name='bills'),
    path('dashboardbillslist/', views.dashboard_bills_list, name='dashboardbillslist'),
    path('dashboardbilldetail/<int:bill_id>/', views.dashboard_bill_detail, name='dashboardbilldetail'),
    path('politicianbio/', views.politician_bio, name='politicianbio'),

    path('error404/', views.error404, name='error404'),
    path('error500/', views.error500, name='error500'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('faq/', views.faq, name='faq'),
]
