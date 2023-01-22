#Import django https 
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie 


# Create your views here.

#Put https request in the function 
def index (request): 
    movies = Movie.objects.all()
    return(render(request, 'index.html', {'movies' :movies }))

    


#Adding URLs > Creating new urls.py in the app folders 