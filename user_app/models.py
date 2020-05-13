from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import User
# Validate Username & Email
username_validator = UnicodeUsernameValidator()

def validate_email_unique(email_id):
    exists = User.objects.filter(email=email_id)
    if exists:
        raise ValidationError("Email address %s already exists" % email_id)

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=150, min_length=4,validators=[username_validator],
                            help_text='Required. 150 characters or fewer.',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50,validators =[validate_email_unique], help_text='Required. Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password1 = forms.CharField(label='Password',widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                            help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                            help_text=('Just Enter the same password, for confirmation'))

    def save(self,commit=True):
        user = super(UserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
        }
    def save(self,commit=True):
        user = super(UserProfileChange,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    address = models.CharField(max_length=255,blank=True,null=True)
    contact = models.IntegerField(blank=True,null=True)
    avatar = models.ImageField(upload_to='images',blank=True,null=True)
    def __str__(self):
        return self.user.username

    objects = models.Manager

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address','contact','avatar')
        widgets = {
            'address':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Address',
                'autofocus':'True',
                'tabindex':'1',
            }),
            'contact':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Contact',
                'tabindex':'2',
            }),
            'avatar':forms.FileInput(attrs={
                'class':'form-control',
                'placeholder':'Select Image',
                'tabindex':'3',
            })
        }
