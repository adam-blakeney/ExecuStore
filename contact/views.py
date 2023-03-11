from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings


# Create your views here.


def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been recieved!')
        else:
            messages.warning(request, 'Please fill out form fully')

    return render(request, 'contact.html')