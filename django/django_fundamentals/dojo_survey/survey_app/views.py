from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "form.html")

def process(request):
    # print(request.method) #Confirms this is a POST method
    if request.method == "POST":
        context = {
            'name': request.POST['user_name'],
            'loc': request.POST['location'],
            'lang': request.POST['language']
        }
        return render(request, "result.html", context)
    return render(request, "result.html")
    