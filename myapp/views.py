from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from myapp.forms import userForm, messageForm
from myapp.models import user, message_format
from django.db import utils
from twilio.base.exceptions import TwilioRestException
import datetime

# Home Page feature
def home(request):
    users_list = user.objects.all()
    return render(request,'home.html',{'user_list':users_list})

# Add User feature
def add(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/home')
            except Exception as e:
                return HttpResponse("Exception: "+ str(e))
        else:
            return HttpResponse("Invalid Data:" + str(form.errors.as_data()))
    else:
        form = userForm()
    return render(request,'add.html',{'form':form})

# Delete User feature
def destroy(request,id):
    user_list = user.objects.get(id=id)
    user_list.delete()
    return redirect("/home")

# Edit User feature
def edit(request, id):
    user_list = user.objects.get(id=id)
    return render(request,'edit.html', {'user':user_list})

def edit_save(request, id):
    user_list = user.objects.get(id=id)
    form = userForm(request.POST, instance = user_list)
    if form.is_valid():
        try:
            form.save()
            return redirect("/home")
        except Exception as e:
            return HttpResponse("Exception: "+ str(e))
    else:
        return HttpResponse("Invalid Data:" + str(form.errors.as_data()))
    return render(request, 'edit.html', {'user': user_list})

# Send SMS feature
def sendsms(request, id):
    #if request.method == 'POST' and 'send_a_sms' in request.POST:
        User = user.objects.get(id=id)
        name = User.name
        phone = User.phone
        from send_sms import sms
        try:
            sms(name,phone)
            success_inc(id)
        except TwilioRestException as e:
            error_inc(id)
            return HttpResponse("TwilioRestException" + str(e))
        except Exception as ex:
            error_inc(id)
            return HttpResponse("Exception" + str(ex))
        return redirect("/home")
    #else:
        #return HttpResponse("Wrong submit request")

def success_inc(id):
    record = user.objects.get(id=id)
    value = record.success + 1
    record.success = value
    record.last_sms = datetime.datetime.now()
    record.save()

def error_inc(id):
    record = user.objects.get(id=id)
    value = record.error + 1
    record.error = value
    record.save()

# Message Format feature
def message(request):
    #if request.method == 'POST' and 'message_button' in request.POST:
    Message = message_format.objects.latest('id')
    message_list = message_format.objects.all()
    #print(Message)
    return render(request,'message.html',{'message_format':Message,'message_list':message_list})

def message_save(request):
    Message = message_format.objects.latest('id')
    Form = messageForm(request.POST)
    if Form.is_valid():
        try:
            Form.save()
            return redirect("/home")
        except Exception as e:
            return HttpResponse("Exception: "+ str(e))
    else:
        return HttpResponse("Invalid Data:" + str(Form.errors.as_data()))
    return render(request, 'message.html', {'message_format':Message})
