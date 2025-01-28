from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm

# Create your views here.
def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, 
              "Thanks for getting in contact! We will aim to get in touch as soon as possible.")
            contact_form = ContactForm()  # Reset the form after saving

    return render(
        request,
        "about/about.html",
        {"about": about, "contact_form": contact_form},
    )