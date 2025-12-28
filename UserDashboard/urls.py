from django.urls import path
from .views import *

urlpatterns = [
    path('', userDashboard, name='UserDashboard'),
    path('complaintForm', complaintForm, name='complaintForm'),
]