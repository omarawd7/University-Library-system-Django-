from django.urls import path 
from .import views


urlpatterns = [
 
   path('',views.index, name='index'),
   path('about/',views.about, name='about'),
   path('Log_in/',views.Log_in, name='Log_in'),
   path('logout/',views.logoutUser, name='logout'),
   path('Sign_Up/',views.Sign_Up, name='Sign_Up'),
   path('Search/',views.Search, name='Search'),
   path('books/',views.books,name='books'),
   path('Search/Log_in/',views.Log_in, name='Log_in'),
   path('Search/about/',views.about),
   path('Search/Sign_Up/',views.Sign_Up),
]
