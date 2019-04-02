from django.http import HttpResponse
from django.shortcuts import render
import time as t
from .forms import FoodForm

from .models import sdata, Foodname
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'canteen/home.html')


def about(request):
    return render(request, 'canteen/about.html')


def gallery(request):
    return render(request, 'canteen/gallery.html')


def index(request):
    return HttpResponse('<h2>Hii</h2>')


def redirect(request):
    return render(request, 'canteen/register.html')


def register(request):
    name = request.POST["name"]
    password = request.POST["password"]
    sapid = request.POST["sapid"]
    dept = request.POST["dept"]
    phone = request.POST["phone"]
    email = request.POST["email"]

    studentdata = sdata(name=name, sapid=sapid, phone=phone, dept=dept, email=email, password=password)
    studentdata.save()

    return render(request, 'canteen/thanks.html', {'name': name})


def index(request):
    return render(request , 'canteen/login.html')


def login(request):
    name = request.POST['lname']
    password = request.POST['lpass']
    dataset =sdata.objects.all()

    try:
        selected = dataset.get(name=name)
        print("student Found")
    except Exception as e:
        return render(request, 'canteen/thanks.html')


    if(password == selected.password):
        ti = t.time()
        t3600 = ti+3600
        return render(request, 'canteen/response.html', {'dataset': dataset, 't3600': t3600})


def food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)

    form = FoodForm()
    return render(request, 'canteen/forms.html', {'form': form})
