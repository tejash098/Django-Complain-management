from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Complaint(models.Model):

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    )

    CATEGORY_CHOICES = (
        ('WATER', 'Water Issue'),
        ('ROAD', 'Road Damage'),
        ('ELECTRICITY', 'Electricity'),
        ('GARBAGE', 'Garbage Collection'),
        ('STREET_LIGHT', 'Street Light'),
        ('INTERNET', 'Internet'),
        ('OTHER', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    admin_remark = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='complaints/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
