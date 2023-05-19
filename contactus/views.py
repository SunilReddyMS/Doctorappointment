from django.shortcuts import render

from .models import contactus

# Create your views here.


def contactus(request):
      if request.method=="POST":
          name=request.POST.get('name')
          number=request.POST.get('number')
          email=request.POST.get('email')
          options=request.POST.get('options')
          message=request.POST.get('message')
          upload=request.POST.get('upload')
          contact=contactus(name=name,number=number,email=email,options=options,message=message,upload=upload)
          contact.save()    
      return render(request, "contact.html") 
    
         
   
         







 

