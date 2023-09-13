from django.shortcuts import render
from django.http import HttpResponse
from contactslist.models import Contact
# Create your views here.

def index(request):

    return HttpResponse("Hello!")

def display(request):

    contacts = Contact.objects.all()
    s = ""
    
    for c in contacts:
        s = s+c.to_string()+'<br>'
    return HttpResponse("<strong>Contacts:</strong><br>"+s) 
