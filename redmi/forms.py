from django import forms
from .models import Redmi

class RedmiForm(forms.ModelForm):

    class Meta:
        model = Redmi
        fields = '__all__'