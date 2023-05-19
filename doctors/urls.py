from django.urls import path
from . import views

urlpatterns = [
    path("doctor",views.doctor, name="doctor" ),
    path("doctorlogin",views.doctorlogin, name="doctorlogin" ),
    path("doctorsignup",views.doctorsignup, name="doctorsignup" ),
   
   
]
