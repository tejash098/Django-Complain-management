from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from UserDashboard.models import Complaint 
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.timezone import now
from datetime import datetime, timedelta

@login_required(login_url='login')
def AdminDashboard(request):
    complaints = Complaint.objects.all()
    totalComplaints = Complaint.objects.count()
    pendingComplaints = Complaint.objects.filter(status = 'PENDING').count()
    inProgressComplaints = Complaint.objects.filter(status = 'IN_PROGRESS').count()
    resolvedComplaints = Complaint.objects.filter(status = 'RESOLVED').count()

    resolutionRate = (
        (resolvedComplaints / totalComplaints) * 100
        if totalComplaints > 0 else 0
    )

    last_7_days = now() - timedelta(days=7)
    recentComplaints = complaints.filter(created_at__gte=last_7_days).count()

    return render(request, 'AdminDashboard/AdminDashboard.html', {"complaints" : complaints, 
    "totalComplaints" : totalComplaints, 
    "pendingComplaints" : pendingComplaints, 
    "inProgressComplaints" : inProgressComplaints, 
    "resolvedComplaints" : resolvedComplaints,
    "resolutionRate" : round(resolutionRate,1),
    "recentComplaints" : recentComplaints})

@login_required(login_url='login')
def complaint_detail(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    if request.method == "POST":
        complaint.status = request.POST.get('status')
        complaint.admin_remark = request.POST.get('admin_remark')
        complaint.save()
        return redirect('AdminDashboard')
    return render(request, 'AdminDashboard/complaint_detail.html', {'complaint': complaint})
