import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class ControlPageForm(forms.Form):
  url = forms.URLField(
    label='URL',
    widget=forms.TextInput(attrs={'size': 64})
  )
  title = forms.CharField(
    label='Title',
    widget=forms.TextInput(attrs={'size': 64})
  )
  tags = forms.CharField(
    label='Tags',
    required=False,
    widget=forms.TextInput(attrs={'size': 64})
  )