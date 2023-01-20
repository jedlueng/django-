#Import django https 
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#Put https request in the function 
def index (request): 
    return HttpResponse("Hello World ")


#Adding URLs > Creating new urls.py in the app folders 