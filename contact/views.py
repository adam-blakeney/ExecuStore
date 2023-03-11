from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse

# Create your views here.


def Contact(request):
    if request.method == "POST":
        Contact = Contact()
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        contact_email = request.POST.get('contact_email')
        subject = request.POST.get('subject')
        contact.first_name = first_name
        contact.second_name = second_name
        contact.contact_email = contact_email
        contact.subject = subject
        contact.save()
        return messages.success(request, 'Your message has been recieved!')
    return render(request, 'contact.html')