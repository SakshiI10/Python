from django.shortcuts import render, HttpResponse

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
    return render(request, 'contact.html')