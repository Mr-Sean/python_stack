import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show, User, UserManager, ShowManager
import bcrypt

context = {
    'shows': Show.objects.all()
}

# LOGIN AND REG SECTION BELOW #

# render the INDEX page
def index(request):
    request.session.flush()
    return render(request, 'index.html')


# validate registration
def register(request): # post redirect
    if request.method == 'POST':
        errors = User.objects.reg_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        # hash the pw
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

        # create a user
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hashed_pw
        )
        # create a session
        request.session['user_id'] = new_user.id
        return redirect('/success')
    return redirect('/')

# render SUCCESS page

# log in
def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/success')
    return redirect('/')
    
# log out
def logout(request):
    request.session.flush()
    return redirect('/')


# SEMI-RESTFUL SECTION BELOW #

def new(request):
    return render(request, "new.html")

def create(request):
    # CREATE THE SHOW
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/success/new') # use "/" b4 "success/new". "/" not needed in URLS.PY
    
    new_show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    request.session['shows'] = new_show.id
    return redirect("/success")

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')

    # this_user = User.objects.filter(id=request.session['user_id'])
    
    context = {
        'user_id': User.objects.get(id=request.session['user_id']),
        "shows" : Show.objects.all()
        # 'user': this_user[0]
        # 'shows': Show.objects.all()
    }
    return render(request, 'success.html', context)

def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        "show": one_show
    }
    return render(request, "edit.html", context)
    # return render(request, "edit.html")

def update(request, show_id):
    
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit') # use "/" b4 "shows/{show_id}/edit". "/" not needed in URLS.PY
    
    # Update a Show
    to_update = Show.objects.get(id=show_id)
    # Updates each Field
    print(to_update)
    to_update.title = request.POST['title']
    to_update.release_date = request.POST['release_date']
    to_update.network = request.POST['network']
    to_update.description = request.POST['description']
    to_update.save()

    return redirect(f'/shows/{to_update.id}')


def show(request, show_id):
    # Query for 1 show with show_id
    one_show = Show.objects.get(id=show_id)
    context = {
        "show": one_show
    }
    return render(request, "show.html", context)
    # return render(request, "show.html")

def delete(request, show_id):
    # NOTE: Deletes 1 show
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect("/success")
