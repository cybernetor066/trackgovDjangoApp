import time, bson, json, os, sys, datetime, string, random

from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.core import mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings
from django.template import loader

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, pagination
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger


from .models import UserRegistration, HouseOfRepsBills
from .forms import UserRegistrationForm, UserLoginForm

from bson import ObjectId
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import dns


# Accessing files in directories
if getattr(sys, 'frozen', False):
    # running in a bundled form
    base_dir = sys._MEIPASS # pylint: disable=no-member
else:
    # running normally
    base_dir = os.path.dirname(os.path.abspath(__file__))

# Getting our connection strings, both for mongo and redis and other enviroment variables
load_dotenv()

connection_string_mongo = os.environ['MY_CONNECTION_STRING_MONGO']



file_path = os.path.join(base_dir, 'static/trackgovApp/uploads/images')


# Create your views here.
# def index(request):
#     template = loader.get_template('trackgovApp/index.html')
#     context = {
#         'greeting': 'Hello Overlord!!',
#     }
#     return HttpResponse(template.render(context, request))

# Or we use a render
def index(request):
    return render(request, 'trackgovApp/index.html')


# home view
def home(request):
    return render(request, 'trackgovApp/home.html')


# login view
def login(request):
    if request.method =='POST':
        # print("HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!")
        form =  UserLoginForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Confirmations
            print("Details are: '%s' as your username" % username)
            print("And : '%s' as your phone" % password)

            # Then perform our database query
            pass


    form = UserLoginForm()
    return render(request, 'trackgovApp/login.html', {"form": form})


# logout view
def logout(request):
    return render(request, 'trackgovApp/logout.html')




# signup view
def signup(request):
    if request.method =='POST':
        # print("HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!")
        form =  UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # firstname = form.cleaned_data['firstname']
            # lastname = form.cleaned_data['lastname']
            useremail = form.cleaned_data['useremail']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Confirmations
            # print("Thank you user! you entered : '%s' as your firstname" % firstname)
            # print("And : '%s' as your lastname" % lastname)
            print("And selected : '%s' as your username" % useremail)
            print("And: '%s' as your username" % username)
            print("And : '%s' as your phone" % password)


            # # # send to our email(Basic email)
            # subject = 'Your Django Test Email(Latest Test)'
            # message = 'Hello Support Goodday! \
            #             This is a Django Test Project Email Test!! \
            #             Here are the user form details entered : \
            #             First name : %s \
            #             Last name : %s \
            #             User Email : %s \
            #             Username : %s And \
            #             Password : %s \
            #             ' % (firstname, lastname, useremail, username, password)
            # from_email = "spacenetngbase@gmail.com"      # Or the admin email address
            # to_email = useremail                        # Or the admin email addres (Same thing here)
            # send_mail(subject, message, from_email, [to_email,], fail_silently=False,)


            # # send to our email(Email with attachment)
            # subject = 'Your Django Test Email(Latest Test)'
            # message = 'Hello Support Goodday! \
            #             This is a Django Test Project Email Test!! \
            #             Here are the user form details entered : \
            #             First name : %s \
            #             Last name : %s \
            #             User Email : %s \
            #             Username : %s And \
            #             Password : %s \
            #             ' % (firstname, lastname, useremail, username, password)
            # from_email = "spacenetngbase@gmail.com"      # Or the admin email address
            # to_email = useremail                        # Or the admin email addres (Same thing here)
            # if subject and message and from_email:
            #     try:
            #         email_msg = EmailMessage(
            #             subject, message, from_email, [to_email,]
            #             )
            #         # img_data = open(file_path, 'rb').read()
            #         # email_msg.attach('your_image.jpg', img_data)
            #         email_msg.attach_file(file_path)
            #         email_msg.send()

            #     except BadHeaderError:
            #         return HttpResponse('Invalid header found.')

            # Then perform database operation
            form.save()

            # confirm operation successfull
            print('User records saved successfully!!!')

    form = UserRegistrationForm()
    return render(request, 'trackgovApp/signup.html', {"form": form})




# recover password view
def recoverpw(request):
    if request.method =='POST':
        # print("HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!")
        form =  UserLoginForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Confirmations
            print("Details are: '%s' as your username" % username)
            print("And : '%s' as your phone" % password)

            # Then perform our database query
            pass


    form = UserLoginForm()
    return render(request, 'trackgovApp/recoverpw.html', {"form": form})




# categories view
def categories(request):
    return render(request, 'trackgovApp/categories.html')


# Dashboard view
def dashboard(request):
    return render(request, 'trackgovApp/dashboard.html')









# Dashboard starter view
def dashboard_starter(request):
    return render(request, 'trackgovApp/starter.html')

# Dashboard order details view
def dashboard_bill_progress(request):
    return render(request, 'trackgovApp/bills-progress.html')









# # Dashboard bills list page view
# def dashboard_bills_list(request):
#     return render(request, 'trackgovApp/bills-list.html')



# bills view
def bills(request):
    return render(request, 'trackgovApp/bills.html')


# Dashboard bills list page view
def dashboard_bills_list(request):
    # context = { 
    #     'ourRange0': range(3),
    #     'ourRange1': range(9)
    #     }
    bill_list = HouseOfRepsBills.objects.all()
    context = {
        'bill_list': bill_list
    }
    return render(request, 'trackgovApp/bills-list.html', context=context)


# Dashboard bills detail page view
def dashboard_bill_detail(request):
    context = { 
        'ourRange0': range(3),
        'ourRange1': range(9)
        }
    return render(request, 'trackgovApp/bill-detail.html', context=context)

# politician's bio view
def politician_bio(request):
    return render(request, 'trackgovApp/politician-bio.html')


# error 404 function
def error404(request):
    return render(request, 'trackgovApp/error-404.html')

# error 500 function
def error500(request):
    return render(request, 'trackgovApp/error-500.html')

# maintenance function
def maintenance(request):
    return render(request, 'trackgovApp/maintenance.html')

# faq function
def faq(request):
    return render(request, 'trackgovApp/faq.html')




# def handle_upload_file(file):
#     with open(file_path +file.name,'wb+') as destination:  # Not good to hardcode file paths when programming
#         for chunk in file.chunks():
#             destination.write(chunk)