from django import forms
from myapp.models import user,message_format

class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = "__all__"

class messageForm(forms.ModelForm):
    class Meta:
        model = message_format
        fields = "__all__"
