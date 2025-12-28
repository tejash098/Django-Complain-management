from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profile
# Create your views here.

@login_required(login_url='login')
def userDashboard(request):
    user = request.user
    userRole = Profile.objects.get(user = user)
    return render(request, 'Userdashboard/UserDashboard.html', {'user': user, 'userRole': userRole.role})
