from django.db import models

# Create your models here.

class cat_db(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Desc = models.CharField(max_length=200,null=True,blank=True)
    Imge = models.ImageField(upload_to="image",null=True,blank=True)

class prod_db(models.Model):
    Cname = models.CharField(max_length=100,null=True,blank=True)
    Pname = models.CharField(max_length=100,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Descp = models.CharField(max_length=100,null=True,blank=True)
    Imges = models.ImageField(upload_to="proImages",null=True,blank=True)