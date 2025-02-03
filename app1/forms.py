from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Visitor

class CreateRecord(forms.Form):

    coordinator_name = forms.CharField(max_length=50)
    coordinator_phone = forms.CharField(max_length=15)
    visitor_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=15)
    organization = forms.CharField(max_length=100)
    location = forms.CharField(max_length=50)
    domain = forms.CharField(max_length=50)
    event = forms.CharField(max_length=100)
    date = forms.DateField()

class VisitorEditForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'organization','phone', 'location', 'domain', 'event', 'date']

