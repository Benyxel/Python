from django import forms
from .models import demoappModel

class demoappForm(forms.ModelForm):
    class Meta:
        model = demoappModel
        fields = ['name','email','phone','address']