from django.db import models
from django.db.models import Count,Sum,Max,Min,Avg
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.core import validators

class Customer(models.Model):
    def contact_validator(contact):
        if len(contact) != 10:
            raise validators.ValidationError('Contact length should be 10 digit')
    def min_length_validator(name):
        if len(name) < 1:
            raise validators.ValidationError('Minimum length should be 1 letter')

    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=30,unique=True,validators=[min_length_validator])
    contact = models.CharField(max_length=10,validators=[contact_validator])

    
    def bal_amount(self):
        gave = self.account.all().aggregate(Sum('gave'))['gave__sum']
        got = self.account.all().aggregate(Sum('got'))['got__sum']
        return gave - got

    objects = models.Manager

    def __str__(self):
        return self.name

