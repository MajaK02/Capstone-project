from .models import CollaborateRequest
from django import forms

# Collaboration Form
class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')  