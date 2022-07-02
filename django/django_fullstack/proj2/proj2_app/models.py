from django.db import models
import re
import bcrypt

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        # add keys & values to ERRORS dictionary for each invalid field
        # Length of 1st Name
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name must be at least 2 characters long"

        # Length of Last Name
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name must be at least 2 characters long"

        # Email matches format ("regex" or RE = Regular Expressions Library)
        if len(postData['email']) == 0:
            errors['email'] = 'You must enter an email'
        elif not email_regex.match(postData['email']):
            errors['email'] = 'Must be a valid email'
            
        # Email is Unique
        current_users = User.objects.filter(email = postData['email'])
        if len(current_users) > 0:
            errors['duplicate'] = "That email already exists"

        # Password entered (less LessThan 8)
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long'
        if postData['password'] != postData['confirm_password']:
            errors['mismatch'] = 'Your password does not match'
        return errors

    def login_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(email=postData['email'])
        # email has been entered
        if len(postData['email']) == 0:
            errors['email'] = 'Email must be entered'
        # password has been entered
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        # if email and password match
        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['password'] = 'Email and Password do not match'
        return errors


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # postData == request.POST
        if len(postData['title']) < 3:
            errors['title'] = 'Title must be at least 3 characters long.'
        
        if len(postData['network']) < 3:
            errors['network'] = 'Network must be at least 3 characters long.'
        
        if len(postData['description']) < 3:
            errors['description'] = 'Description must be at least 3 characters long.'
        return errors


class User(models.Model):
    #id
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    password = models.CharField(max_length=255)
    objects = UserManager()


class Show(models.Model):
    #ID
    title = models.CharField(max_length=55)
    network = models.CharField(max_length=55)
    release_date = models.DateTimeField()
    description = models.TextField(default='')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()