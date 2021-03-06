"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
admin.autodiscover()

from myapp.views import home,add,destroy,edit,edit_save,sendsms,message,message_save

urlpatterns=[
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home, name = 'home'),
    url(r'^add/', add, name = 'add'),
    url(r'^message/', message, name = 'message'),
    url(r'^message_save/', message_save, name = 'message_save'),
    url(r'^delete/(?P<id>[\d]+)/$', destroy, name='destroy'),
    url(r'^edit/(?P<id>[\d]+)/$', edit, name = 'edit'),
    url(r'^edit_save/(?P<id>[\d]+)/$', edit_save, name = 'edit_save'),
    url(r'^sendsms/(?P<id>[\d]+)/$', sendsms, name = 'sendsms'),
]
