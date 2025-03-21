from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name="app"),
    path('data/', views.myapp_data, name='app_data'),
    path('data/<int:course_id>/', views.details_page, name="course_detail")
]