from django.contrib import admin
from django.urls import path,include
from django.conf.urls import  url
from . import views


urlpatterns = [
   
    path('postComment',views.postComment,name="postComment"),
    path('', views.bloghome, name='bloghome'),
    path('createposts', views.createposts, name='createposts'),
    path('<str:slug>', views.blogpost, name='blogpost'),
  
    
    
  

]
