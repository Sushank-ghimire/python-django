from django.shortcuts import render
from .models import AppVariety
from django.shortcuts import get_object_or_404
from .forms import AppVarietyForm

# Create your views here.
def app(request):
    return render(request, "myapp/app.html")

def myapp_data(request):
    all_data = AppVariety.objects.all()
    return render(request, "apps.html", {'app_data': all_data})

def details_page(request, course_id):
    app = get_object_or_404(AppVariety, pk=course_id)
    return render(request, "details.html", { 'data' : app })

def app_store(request):
    stores = None
    if request.method == 'POST':
        form = AppVarietyForm(request.POST)
        if form.is_valid():
            form.cleaned_data['app_variety']
            app_variety = AppVariety.objects.all()
            stores = app_variety
    else:
        form = AppVarietyForm()
    if request.method == "GET":
        return render(request, 'app_store.html', { 'stores': stores, 'form': form })
    return render(request, 'app_store.html', { 'stores': stores, 'form': form })