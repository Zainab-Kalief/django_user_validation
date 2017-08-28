from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
NAME_REGEX = re.compile(r'[a-zA-Z0-9.,-]*$')

class UserManager(models.Manager):
    def log_in(self, data):
        password = data['password']
        if self.filter(email=data['email']):
            user = self.get(email=data['email'])
            hash_password = bcrypt.hashpw(password.encode(), user.password.encode())
            if (hash_password == user.password):
                print user, user.password, hash_password
                return user
            else:
                return False
        else:
            return False

    def register(self, data):
        errors = {}
        if not (NAME_REGEX.match(data['name']) and len(data['name'])):
            errors['name'] = 'Please enter a real name'
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = 'Please enter an authentic email e.g xxxx@yahoo.com'
        if self.filter(email=data['email']):
            errors['email_exist'] = 'Email Already exists'
        if len(data['password']) < 8:
            errors['password'] = 'Your password must be 8 characters or more'
        if data['confirm_password'] != data['password']:
            errors['confirm_password'] = 'Your password doesnt match'

        if len(errors):
            return errors
        else:
            user_password = data['password']
            user_password = user_password.encode()
            hash_password = bcrypt.hashpw(user_password, bcrypt.gensalt())
            return self.create(name=data['name'], email=data['email'], password=hash_password)

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = UserManager()
