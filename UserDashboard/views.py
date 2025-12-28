from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profile
from .models import Complaint
from django.shortcuts import redirect
from .forms import ComplaintForm
# Create your views here.

@login_required(login_url='login')
def userDashboard(request):
    user = request.user
    userRole = Profile.objects.get(user = user)
    complaints = Complaint.objects.filter(user = user)
    totalComplaints = Complaint.objects.filter(user = user).count()
    pendingComplaints = Complaint.objects.filter(user = user, status = 'PENDING').count()
    inProgressComplaints = Complaint.objects.filter(user = user, status = 'IN_PROGRESS').count()
    resolvedComplaints = Complaint.objects.filter(user = user, status = 'RESOLVED').count()
    
    return render(request, 'Userdashboard/UserDashboard.html', {'user': user, 
    'userRole': userRole.role, 
    'complaints': complaints,
    'totalComplaints': totalComplaints,
    'pendingComplaints': pendingComplaints,
    'inProgressComplaints': inProgressComplaints,
    'resolvedComplaints': resolvedComplaints})

@login_required(login_url='login')
def complaintForm(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            user = request.user
            complaint.user = user
            complaint.save()
        return redirect('UserDashboard')
    else:
        form = ComplaintForm()
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        return render(request, 'Userdashboard/ComplaintForm.html', {'form': form})