from dataclasses import fields
from django import forms

class fillForm(forms.Form):
    eid = forms.IntegerField(label = 'Enter the roll no : ' )
    name = forms.CharField(label = 'Enter the name : ' , max_length= 30)
    school = forms.ChoiceField(choices=((1,'male') , (2,'female') , (3,'transgender')))