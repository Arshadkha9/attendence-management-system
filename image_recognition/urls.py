# myapp/urls.py
from django.urls import path
from image_recognition import views


urlpatterns = [
    path('check_image/<int:id>/', views.check_image, name='check_image'),
    
    # Add more URL patterns as needed
]