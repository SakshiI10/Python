from django.shortcuts import render, HttpResponse
# Added manually for submitting form in database
from datetime import datetime
from .models import Contact 

# Create your views here manually.
def index(request):
    # return HttpResponse("This is homepage")
    context={
        "variable1":"1234567890",
        "variable2":"9876543210"
    }
    return render(request, 'index.html', context)

def about(request):
    # return HttpResponse("This is about")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("This is services")
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("This is contact") 

    # If you want to store your form in database, then this is the logic:
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())

        contact.save()
    return render(request, 'contact.html')