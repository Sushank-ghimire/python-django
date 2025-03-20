from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world from django app")

def about(request):
    return HttpResponse("Hello at about route in django app")

def contact(request):
    return HttpResponse("Hello at contact route of the django app")