from django.db import models

# Create your models here.

class contactus(models.Model):
  name = models.CharField(max_length=255)
  number=models.IntegerField()
  email=models.EmailField(max_length=255)

  option =(
    ("doctorappointment", "doctorappointment"),
    ("labtest", "labtest"),   
)
  
  options = models.CharField( max_length = 20,  choices = option)
  message = models.TextField( )
  upload = models.FileField()
        
       
  