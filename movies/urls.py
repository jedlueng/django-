#First we need to get path 
from django.urls import path
# Need to import view to this file 
from . import views



#Make a list of url patterns 
# '' = endpoint 
# movies/
 
#URL configuration 
urlpatterns  = [
    path('',views.index, name = 'index' )
]


#Next you need to use this in your main application 
#urls.py on the main application folder 