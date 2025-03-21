from django.shortcuts import render
from .models import AppVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def app(request):
    return render(request, "myapp/app.html")

def myapp_data(request):
    all_data = AppVariety.objects.all()
    return render(request, "apps.html", {'app_data': all_data})

def details_page(request, course_id):
    app = get_object_or_404(AppVariety, pk=course_id)
    return render(request, "details.html", { 'data' : app })