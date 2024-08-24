from django.urls import path
from . import views
#from FoodCaloriesApp import views
urlpatterns = [
   
    path('',views.home),
    #path('currency',views.currency)
]
