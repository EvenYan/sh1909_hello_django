from django.http import HttpResponse
from django.shortcuts import render
from contact.models import Contact

# Create your views here.


def home(request):
    return HttpResponse("Hello Django")


def index(request):
    contact_list = Contact.objects.all()
    return render(request, "contact/index.html", context={"contact_list": contact_list})