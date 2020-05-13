from .models import Account
from django import forms


class GaveForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('desc','gave','customer')
        widgets = {
            'desc':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Description',
                'autofocus':'True',
                'tabindex':'1',
            }),
            'gave':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Amount you gave',
                'tabindex':'2',
            })
        }

class GotForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('desc','got','customer')
        widgets = {
            'desc':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Description',
                'tabindex':'1',
            }),
            'got':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Amount you got',
                'tabindex':'2',
            })
        }