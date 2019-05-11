from django.db import models
import os
from django.contrib.auth.models import User

class categories(models.Model):
    name=models.CharField(max_length=2500)

   

class productowner(models.Model):
    name=models.CharField(max_length=2500)
    phone=models.CharField(max_length=2500)
    emargencephonenumber=models.CharField(max_length=2500)
    profile = models.FileField(upload_to='images/')

    
class image(models.Model):
    profile_product1 = models.FileField(upload_to='images/',null=True)
    profile_product1 = models.FileField(upload_to='images/',null=True)
    profile_product2 = models.FileField(upload_to='images/',null=True)
    profile_product3 = models.FileField(upload_to='images/',null=True)

class product(models.Model):
    title=models.CharField(max_length=2500)
    description=models.CharField(max_length=2500)
    price=models.CharField(max_length=2500)
    categoryfrk = models.ForeignKey(categories,null=True)
    imagefrk=models.ForeignKey(image,null=True)
    productownfrk=models.ForeignKey(productowner,null=True)

  


class  client(models.Model):
    firstname=models.CharField(max_length=2500)
    lastname=models.CharField(max_length=2500)
    username=models.CharField(max_length=2500)
    profile_image = models.FileField(upload_to='images/', null=True)
    email=models.CharField(max_length=2500)
    location=models.CharField(max_length=2500)
class  buyer(models.Model):
    client_id=models.ForeignKey(client,null=True)
    product_list=models.CharField(max_length=2500)
    name_tockenkey=models.CharField(max_length=2500)

class  welcomeimages(models.Model):
    Tittle = models.CharField(max_length=30)
    publish_image_for_present=models.FileField(upload_to='images/', null=True)
    small1_banar=models.FileField(upload_to='images/', null=True)
    small2_banar=models.FileField(upload_to='images/', null=True)
    small3_banar=models.FileField(upload_to='images/', null=True)
    small4_banar=models.FileField(upload_to='images/', null=True)
    small5_banar=models.FileField(upload_to='images/', null=True)
    small6_banar=models.FileField(upload_to='images/', null=True)

class PaymentForm(models.Model):
   fname = models.CharField(max_length = 100)
   lname = models.CharField(max_length = 100)
   email = models.CharField(max_length = 100)
   amount = models.CharField(max_length = 100)
   phonenumber = models.CharField(max_length = 100)
   transaction_code= models.IntegerField()
   # clienttime = forms.CharField(max_length = 100)