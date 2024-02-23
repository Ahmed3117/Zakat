from django.contrib import admin
from django.urls import include, path
app_name='zakah'
from .views import home,addmonth
urlpatterns = [
    path('',home,name="home"),
    path('addmonth/<int:pk>/', addmonth, name="addmonth"),

]