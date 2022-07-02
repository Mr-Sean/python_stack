from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("Hello Class!")

def helloWorld(request):
    return HttpResponse("It's DJANGO TIME!")

def heydude(request, name):
    return HttpResponse("Hello " + name)

def catch_all(request, url):
    return redirect("/helloWorld")  # if it said ("/") instead, it would then redirect to "Hello Class" page

def krustykrab(request):
    context = {
        "menu_item": ["krabby patty", "kelp fries", "chum", "pizza"]
    }
    return render(request, "spongebob.html", context) # "render" always paired with "request"

def submission(request):
    if request.method == "POST":
        print("I have successfully sent in the form") # use PRINT statements to test out the code & make sure everything is connected
        # print(request.POST)
        print(request.POST['user_name']) # adding ['user_name'] to POST will only print User Name and ignore everything else
        # return redirect('/krustykrab')

        # BAD PRACTICE Below
        # NEVER RENDER ON A POST ROUTE (aka - a route you're using request.POST)
        # context = {
        #     'name_from_form': request.POST['user_name'],
        #     'food_from_menu': request.POST['menu_item']
        # }
        # return render(request, "result.html", context)

        # GOOD PRACTICE
        request.session['name'] = request.POST['user_name']
        request.session['food'] = request.POST['menu_item']
        return redirect('/thanks')
    return redirect('/krustykrab')

def thanks(request):
    print(request.session)
    # context = {
    #     'name_from_form': request.session['name'],
    #     'food_from_menu': request.session['food']
    # }
    return render(request, "result.html")