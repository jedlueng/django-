#Import django https 
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie 


# Create your views here.

#Put https request in the function 
def index (request): 
    movies = Movie.objects.all()
    return(render(request, 'movies/index.html', {'movies' :movies }))

def detail(request, movie_id): 
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/detail.html', {'movie' : movie} )

    


#Adding URLs > Creating new urls.py in the app folders 