from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    numbers={
        "num":[1,2,3,4,5,6],
        "fruits":['banana','apple'],
    }

    return render(request, "index.html",numbers)

def about(request):
     return render(request, "about.html")

def booking(request):
     return render(request, "booking.html")

def doctors(request):
     return render(request, "doctor.html")

def contact(request):
    return render(request, "contact.html")

def department(request):
    return render(request, "department.html")
