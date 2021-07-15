from django.shortcuts import render
from .models import Info,Contact

def home(request):
    return render(request,'task_app/home.html')

def info(request):
    inf = Info.objects.all()
    return render(request,'task_app/info.html',{"inf":inf})

def contact(request):
    con = Contact.objects.all()
    return render(request,'task_app/contact.html',{"con":con})

