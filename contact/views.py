from django.http import HttpResponse
from django.shortcuts import render
from contact.models import Contact

# Create your views here.


def home(request):
    return HttpResponse("Hello Django")


def index(request):
    contact_list = Contact.objects.all()
    return render(request, "contact/index.html", context={"contact_list": contact_list})


def detail(request, id):
    people = Contact.objects.get(id=id)
    context = {"people": people}
    return render(request, "contact/detail.html", context=context)


def add_contact(request):
    return render(request, "contact/add_contact.html")


def save_contact(request):
    username = request.POST.get("username")
    phone_num = request.POST.get("phone_num")
    print(username, phone_num)
    contact = Contact.objects.create(name=username, phone_num=phone_num)
    return HttpResponse("姓名为：%s数据存储成功！" % contact.name)