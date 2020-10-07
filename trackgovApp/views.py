from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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


# categories view
def categories(request):
    return render(request, 'trackgovApp/categories.html')


# Dashboard view
def dashboard(request):
    return render(request, 'trackgovApp/dashboard.html')


# Dashboard view
def bills(request):
    return render(request, 'trackgovApp/bills.html')