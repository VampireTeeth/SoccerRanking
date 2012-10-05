'''
Created on Oct 3, 2012

@author: steven
'''
from django import forms

class UserForm(forms.Form):
  username = forms.CharField(max_length=50)
  password = forms.CharField(widget=forms.PasswordInput, max_length=50)
  
class MatchForm(forms.Form):
  host_score = forms.IntegerField(required=True, min_value=0)
  visitor_score = forms.IntegerField(required=True, min_value=0)
  
