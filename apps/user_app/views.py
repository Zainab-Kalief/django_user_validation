# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'user_app/index.html')

def dataTest(request):
    request.session.flush()
    entry = User.objects.register(request.POST)
    if not type(entry) is dict:
        return redirect('users:result', kwargs={'id': entry.id})
    else:
        if 'name' in entry:
            messages.add_message(request, messages.INFO, entry['name'])
        if 'email' in entry:
            messages.add_message(request, messages.INFO, entry['email'])
        if 'password' in entry:
            messages.add_message(request, messages.INFO, entry['password'])
        if 'confirm_password' in entry:
            messages.add_message(request, messages.INFO, entry['confirm_password'])
        if 'email_exist' in entry:
            messages.add_message(request, messages.INFO, entry['email_exist'])
        return redirect('/')

def loginTest(request):
    request.session.flush()
    entry = User.objects.log_in(request.POST) #user loging in
    if entry == False:
        messages.add_message(request, messages.INFO, 'This user doesnt exist')
        return redirect('users:index')
    else:
        print entry.id, entry.name
        request.session['user_id'] = entry.id
        return redirect(reverse('users:result', kwargs={'id': entry.id}))

def result(request, id):
    entry = User.objects.get(id=id) #the whole user object gotten by the id from loginTest func redirection
    request.session['user_name'] = entry.name
    # context = {'messages': Post.objects.all().order_by('-created_at'), 'user_id': entry.id}
    return render(request, 'user_app/result.html')
