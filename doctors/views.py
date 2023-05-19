from django.shortcuts import render

# Create your views here.


def doctor(request):
    return render(request, "doctorlogin.html")

def doctorlogin(request):
    return render(request, "doctorlogin.html")



def doctorsignup(request):
    return render(request, "doctorsignup.html")