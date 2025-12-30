from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from UserDashboard.models import Complaint 
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='login')
def AdminDashboard(request):
    complaints = Complaint.objects.all()
    totalComplaints = Complaint.objects.count()
    pendingComplaints = Complaint.objects.filter(status = 'PENDING').count()
    inProgressComplaints = Complaint.objects.filter(status = 'IN_PROGRESS').count()
    resolvedComplaints = Complaint.objects.filter(status = 'RESOLVED').count()
    return render(request, 'AdminDashboard/AdminDashboard.html', {"complaints" : complaints, 
    "totalComplaints" : totalComplaints, 
    "pendingComplaints" : pendingComplaints, 
    "inProgressComplaints" : inProgressComplaints, 
    "resolvedComplaints" : resolvedComplaints})
