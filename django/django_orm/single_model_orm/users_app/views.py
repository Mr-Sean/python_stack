from django.shortcuts import render, redirect
from . models import *

def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, "index.html", context)

def create_user(request):
    if request.method == 'POST':
        User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email_address=request.POST['email'], age=request.POST['age'])
    return redirect('/')