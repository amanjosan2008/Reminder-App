from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from myapp.forms import userForm
from myapp.models import user
from django.db import utils


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


def update(request, id):
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


def submit(request, id):
    if request.method == 'POST' and 'sendsms' in request.POST:
        User = user.objects.get(id=id)
        name = User.name
        phone = User.phone
        from send_sms import sms
        sms(name,phone)
        return redirect("/home")
