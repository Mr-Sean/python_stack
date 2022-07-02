from django.shortcuts import render, redirect

# Create your views here.

def index(request):
  
    return render(request, "form.html")

def process(request):

    # if request.method == "POST":
    if request.method == "GET":   # using GET instead of POST avoids running unnecessary code below.
        return redirect("/")
    
    
    # must run "python manage.py migrate" in Terminal to enable Sessions
    request.session['name'] = request.POST['user_name']
    request.session['loc'] = request.POST['location']
    request.session['lang'] = request.POST['language']


    return redirect('/result')
    # return render(request, "result.html")

def result(request):
    return render(request, 'result.html')