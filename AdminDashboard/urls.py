from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminDashboard, name='AdminDashboard'),
    path('complaint_detail/<int:complaint_id>', views.complaint_detail, name='complaint_detail')
]