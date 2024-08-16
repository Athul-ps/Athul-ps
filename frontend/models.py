from django.db import models

# Create your models here.

class contact_db(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Msg = models.CharField(max_length=300,null=True,blank=True)


class reg_db(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class Cart_db(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    proname = models.CharField(max_length=100, null=True, blank=True)
    Qty = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    totalprice = models.IntegerField(null=True,blank=True)

class checkout_db(models.Model):
    Fname = models.CharField(max_length=100,null=True,blank=True)
    Lname = models.CharField(max_length=100,null=True,blank=True)
    Addr = models.CharField(max_length=100,null=True,blank=True)
    Town = models.CharField(max_length=100,null=True,blank=True)
    Country = models.CharField(max_length=100,null=True,blank=True)
    passcode = models.IntegerField(null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)


