from .models import Customer
from django import forms


class CustomerForm(forms.ModelForm): 
    class Meta:
        model = Customer
        fields = ('name','contact')
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Name',
                'autofocus':'True',
                'tabindex':'1',
            }),
            'contact':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Contact',
                'tabindex':'2',
            })
        }
