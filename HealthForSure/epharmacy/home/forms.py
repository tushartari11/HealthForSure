from django import forms
from .models import Addnewpatient

class Addnewpatientform(forms.ModelForm):
    class Meta:
        model = Addnewpatient
        fields = ['fullname', 'age', 'gender']