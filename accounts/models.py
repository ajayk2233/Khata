from django.db import models
from django.contrib.auth.models import User
from customer_app.models import Customer
from django.core import validators

class Account(models.Model):
    def validate_amount(val):
        if val < 1:
            raise validators.ValidationError('Amount should be atleast 1')

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True,related_name='account')
    desc = models.CharField(max_length=100)
    gave = models.IntegerField(default=0,validators=[validate_amount])
    got = models.IntegerField(default=0,validators=[validate_amount])
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager
    
    def __str__(self):
        return self.desc