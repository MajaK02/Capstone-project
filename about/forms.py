from .models import ContactRequest
from django import forms

# Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'subject', 'message', 'destination')