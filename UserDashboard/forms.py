from django.forms import ModelForm
from .models import Complaint

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description', 'category', 'image']