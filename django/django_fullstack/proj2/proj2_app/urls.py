from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),

    path('register', views.register),
    
    path('login', views.login),
    
    path('success', views.success),
    
    path('logout', views.logout),

    # localhost:8000/success/new
    path('new', views.new),

    # localhost:8000/success/create
    path('create', views.create),

    # localhost:8000/shows/<show_id>/update
    path('<int:show_id>/update', views.update),

    # localhost:8000/success/<show_id>/edit
    path('<int:show_id>/edit', views.edit),

    # localhost:8000/success/<show_id>
    path('<int:show_id>', views.show),

    # localhost:8000/success/<show_id>/delete
    path('<int:show_id>/delete', views.delete),

]
