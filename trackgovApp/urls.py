from django.urls import path, include

from . import views

# app_name = 'trackgovApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('recoverpw/', views.recoverpw, name='recoverpw'),
    
    path('categories/', views.categories, name='categories'),
    path('dashboardbillslist/', views.dashboard_bills_list, name='dashboardbillslist'),
    # path('dashboardbilldetail/<int:bill_id>/', views.dashboard_bill_detail, name='dashboardbilldetail'),
    path('dashboardbilldetail/<int:bill_id>/<str:rep_name>/', views.dashboard_bill_detail, name='dashboardbilldetail'),

    path('show-loc/', views.show_location, name='showlocation'),

    # path('politicianbio/', views.politician_bio, name='politicianbio'),
    path('politicianbio/<str:rep_name>/', views.politician_bio, name='politicianbio'),

    # path('trackbillspreferences/<int:bill_id>/<str:option>/', views.track_bills_preferences, name='trackbillspreferences'),
    path('trackbillspreferences/', views.track_bills_preferences, name='trackbillspreferences'),
    path('trackbilldetailpreferences/', views.track_billdetail_preferences, name='trackbilldetailpreferences'),

    path('error404/', views.error404, name='error404'),
    path('error500/', views.error500, name='error500'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('faq/', views.faq, name='faq'),
]
