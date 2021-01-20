
from django.contrib import admin
from django.urls import path
from home import views
from .views import services2,Article,contact

urlpatterns = [
   path( "" , views.index , name="home"),
   path('about',views.about, name='about'),
  # path('about' , views.about , name="about")
   #path( "about" , views.about , name="about")
   path( "services" , views.services , name="services"),
   path( "services1",views.services1),
   path( "contact" , contact.as_view() , name="contact"),
   path( "services2", services2.as_view(),name="Services2"),
   path( "article", Article.as_view(), name="Article")
]