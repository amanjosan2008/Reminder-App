from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from myapp.forms import userForm, messageForm
from myapp.models import user,message_format
from django.db import utils
from twilio.base.exceptions import TwilioRestException


def home(request):
    users_list = user.objects.all()
    return render(request,'home.html',{'user_list':users_list})


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


def destroy(request,id):
    user_list = user.objects.get(id=id)
    user_list.delete()
    return redirect("/home")


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


def sendsms(request, id):
    #if request.method == 'POST' and 'send_a_sms' in request.POST:
        User = user.objects.get(id=id)
        name = User.name
        phone = User.phone
        from send_sms import sms
        try:
            sms(name,phone)
        except TwilioRestException as e:
            return HttpResponse("TwilioRestException" + str(e))
        except Exception as ex:
            return HttpResponse("Exception" + str(ex))
        return redirect("/home")
    #else:
        #return HttpResponse("Wrong submit request")


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
