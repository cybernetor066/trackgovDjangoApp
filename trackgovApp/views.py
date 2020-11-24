import time, bson, json, os, sys, datetime, string, random, ast
from urllib.parse import urlencode

from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http.response import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
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


from .models import UserRegistration, HouseOfRepsBills, HrepsPoliticiansInfo
from .forms import UserRegistrationForm, UserLoginForm, CategoriesForm

from bson import ObjectId
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import dns


from shapely.geometry import shape, Point
from django.core.serializers import serialize

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

# getting our geo_gis file for AUS
geo_gis_file_aus = os.path.join(base_dir, 'static/trackgovApp/data/elect_boundaries_gj.json')


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


# Dashboard view
def dashboard(request):
    return render(request, 'trackgovApp/dashboard.html')


# categories view
def categories(request):
    if request.method =='POST':
        # print("HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!")
        form =  CategoriesForm(request.POST, request.FILES)
        if form.is_valid():
            res_data = form.cleaned_data['categories']
            res_lat = form.cleaned_data['lat']
            res_lng = form.cleaned_data['lng']
            # print(res_data)


            # bill_list = HouseOfRepsBills.objects.filter(date__in=['03 Sep 2020', '13 May 2020', '29 May 2020'])
            category_list = []
            for data_item in res_data:
                if 'business' in data_item:
                    category_list.append('Finance')
                    category_list.append('Agriculture')
                    category_list.append('Industry, science, energy and resources')
                    category_list.append('Infrastructure, transport, regional development and communications')
                    category_list.append('Treasury')
                    category_list.append('Communications, Cyber Safety and the Arts')

                elif 'civil_rights' in data_item:
                    category_list.append('Attorney general')
                    category_list.append('Home Affairs')

                elif 'drug_policy' in data_item:
                    category_list.append('Health')

                elif 'economy' in data_item:
                    category_list.append('Education, skills and employment')
                    category_list.append('Foreign Affairs and Trade')
                    category_list.append('Finance')
                    category_list.append('Social Services')
                    category_list.append('Treasury')

                elif 'education' in data_item:
                    category_list.append('Education, skills and employment')
                    # category_list.append('')

                elif 'environment' in data_item:
                    category_list.append('Agriculture')
                    category_list.append('Industry, science, energy and resources')

                elif 'food_water' in data_item:
                    category_list.append('Agriculture')
                    category_list.append('Industry, science, energy and resources')

                elif 'foreign_policy' in data_item:
                    category_list.append('Foreign Affairs and Trade')
                    
                elif 'guns' in data_item:
                    # print('Guns here!!!')
                    category_list.append('Home Affairs')

                elif 'healthcare' in data_item:
                    category_list.append('Health')

                elif 'immigration' in data_item:
                    category_list.append('Home Affairs')

                elif 'indigenous' in data_item:
                    category_list.append('Attorney General')
                    category_list.append('Parliamentary Departments')
                    category_list.append('Prime minister and cabinet')

                elif 'jobs_wages' in data_item:
                    category_list.append('Education skills and employment')

                # elif 'context' in data_item:
                #     category_list.append('Context')

                elif 'law_enforcement' in data_item:
                    category_list.append('Home Affairs')

                elif 'lgbtq' in data_item:
                    category_list.append('Attorney General')

                elif 'media_journalism' in data_item:
                    category_list.append('Infrastructure, transport, regional development and commmunications')
                    category_list.append('Communications, Cyber Safety and the Arts')

                elif 'millitary' in data_item:
                    category_list.append('Defence')
                    category_list.append('Veterans Affairs')

                elif 'public_office' in data_item:
                    category_list.append('Attorney General')
                    category_list.append('Finance')
                    category_list.append('Parliamentary Departments')
                    category_list.append('Prime minister and cabinet')

                elif 'privacy' in data_item:
                    category_list.append('Attorney General')
                    category_list.append('Home Affairs')

                elif 'religion' in data_item:
                    category_list.append('Home Affairs')
                    
                elif 'social_programs' in data_item:
                    category_list.append('Social Services')

                elif 'taxes' in data_item:
                    category_list.append('Treasury')

                elif 'technology' in data_item:
                    category_list.append('Infrastructure, transport, regional development and communications')
                    category_list.append('Communications, Cyber Safety and the Arts')

                else:
                    print('Selected All!')
                    pass

            categories = {
                'lat': res_lat,
                'lng': res_lng,
                'filter_list': category_list
            }
            
            base_url = reverse('dashboardbillslist')
            query_string = urlencode(categories)
            my_url = f'{base_url}?{query_string}'
            return redirect(my_url)

    form = CategoriesForm()
    return render(request, 'trackgovApp/categories.html', {"form": form})


# Dashboard bills list page view
def dashboard_bills_list(request):
    # 1) Location (lat long) are detected. 
    # 2) These lat long search the boundary in which they lie. If user is in Australia it will find a feature. Which is stored in feature_found variable. 
    # 3) you can access state, elect_div and other attributes of shape file using feature_found variable, which contains an object of these

    print('Hello!!!')
    userlocation_lat = float(request.GET.get('lat'))
    userlocation_lng = float(request.GET.get('lng')) 

    # global res_object1
    # res_object1 = {}
    
    print('Lat is: ', userlocation_lat)
    print('Long is: ', userlocation_lng)
    
    global boundaries
    boundaries = None
    with open(geo_gis_file_aus) as f:
        boundaries = json.load(f)
    point = Point(userlocation_lat, userlocation_lng)
    # print(point)

    global feature_found
    feature_found = None
    elect_div = None
    for feature in boundaries['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            feature_found = feature
            elect_div = feature["properties"]["Elect_div"]
            print(elect_div)


    if elect_div is not None:
        # response = serialize('json', HrepsPoliticiansInfo.objects.filter(elec_div__icontains=elect_div))
        res_object1 = HrepsPoliticiansInfo.objects.filter(elec_div__icontains=elect_div)
        print(len(res_object1))
        # context = {
        #     'ourRange0': range(3),
        #     'bio_object': response_object[0]
        # }

        if len(res_object1) == 0:
            # return JsonResponse("Electoral div '" + elect_div + "' not found in excel sheet.", safe=False)
            print("Electoral div '" + elect_div + "' not found in excel sheet.")
            pass

    else:
        pass



    # Filtering out the categories
    # list_filter = []
    category_list = request.GET.get('filter_list')
    category_list = ast.literal_eval(category_list)  # make it return to its original object form rather than as string
    if category_list == None:
        print('List is empty: ', category_list)
        # bill_list = HouseOfRepsBills.objects.all()
        res_object2 = HouseOfRepsBills.objects.filter(category__in=category_list)

    else:
        print('List is not empty: ', category_list)
        res_object2 = HouseOfRepsBills.objects.filter(category__in=category_list)




    context = {
        'ourRange0': range(3),
        'bio_object': res_object1[0],
        'bill_list': res_object2
    }        
    return render(request, 'trackgovApp/bills-list.html', context=context)




# Dashboard bills detail page view
def dashboard_bill_detail(request, bill_id):
    context = {
        'bill': get_object_or_404(HouseOfRepsBills, pk=bill_id)
    }
    return render(request, 'trackgovApp/bill-detail.html', context=context)






def show_location(request):
    return render(request, 'trackgovApp/userlocation.html')

# politician's bio view
def politician_bio(request):
    # 1) Location (lat long) are detected. 
    # 2) These lat long search the boundary in which they lie. If user is in Australia it will find a feature. Which is stored in feature_found variable. 
    # 3) you can access state, elect_div and other attributes of shape file using feature_found variable, which contains an object of these
    
    # in JsonResponse(response, safe=false)
    # This will give you actual response that is formed by serializer. 
    # It has some other information, but we need only fields data.
    # Thats why i have returned response[0][‘fields’]
        
    if request.method == 'GET':
        # userlocation_lat = int(float(request.GET['lat']))
        # userlocation_lng = int(float(request.GET['lng']))

        userlocation_lat = float(request.GET['lat'])
        userlocation_lng = float(request.GET['lng'])
        
        print('Hello!')

        print('Lat is: ', userlocation_lat)
        print('Long is: ', userlocation_lng)
        # test_gis_list = [[], []]
        
        global boundaries
        boundaries = None
        with open(geo_gis_file_aus) as f:
            boundaries = json.load(f)
        point = Point(userlocation_lat, userlocation_lng)
        # print(point)

        global feature_found
        feature_found = None
        elect_div = None
        for feature in boundaries['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                feature_found = feature
                elect_div = feature["properties"]["Elect_div"]
                print(elect_div)

        if elect_div is not None:
            # response = serialize('json', HrepsPoliticiansInfo.objects.filter(elec_div__icontains=elect_div))
            response_object = HrepsPoliticiansInfo.objects.filter(elec_div__icontains=elect_div)
            # print(len(response_object))
            context = {
                'ourRange0': range(3),
                'bio_object': response_object[0]
            }

            if len(response_object) == 0:
                return JsonResponse("Electoral div '" + elect_div + "' not found in excel sheet.", safe=False)
            return render(request, 'trackgovApp/politician-bio.html', context=context)

            # Perform our model filtering operation using the "elect_div" as our filtering constraint

        else:
            return JsonResponse("User Do not lie in any electoral division of Australia", safe=False)
    else:
        return HttpResponseBadRequest()

    # return render(request, 'trackgovApp/politician-bio.html')



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