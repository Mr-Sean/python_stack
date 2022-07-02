import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment, User, UserManager, Message
import bcrypt

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
        return redirect('/wall')
    return redirect('/')

# render wall page
def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')

    this_user = User.objects.filter(id=request.session['user_id'])

    context = {
        'user': this_user[0],
        'wall_messages': Message.objects.all()
    }
    return render(request, 'wall.html', context)

def post_message(request):
    if request.method == 'POST':
        errors = Message.objects.message_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Message.objects.create(
                message=request.POST['message'], 
                poster=User.objects.get(id=request.session['user_id'])
            )
    return redirect('/wall')

def post_comment(request, wall_message_id):
    if request.method == 'POST':
        errors = Comment.objects.comment_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Comment.objects.create(
                comment=request.POST['comment'], 
                poster=User.objects.get(id=request.session['user_id']), 
                wall_message=Message.objects.get(id=wall_message_id)
            )
    return redirect('/wall')

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
        return redirect('/wall')
    return redirect('/')
    
def delete_message(request, wall_message_id):
    if request.method == 'POST':
        wall_message = Message.objects.get(id=wall_message_id)
        wall_message.delete()
    return redirect('/wall')

def delete_comment(request, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
    return redirect('/wall')

# log out
def logout(request):
    request.session.flush()
    return redirect('/')