from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, "shows.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    # CREATE THE SHOW
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new') # use "/" b4 "shows/new". "/" not needed in URLS.PY
    
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect("/shows")



def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        "show": one_show
    }
    return render(request, "edit.html", context)

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

def delete(request, show_id):
    # NOTE: Deletes 1 show
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect("/shows")