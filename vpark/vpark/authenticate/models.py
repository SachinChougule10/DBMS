from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
class User_Signup(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_content')
    name = get_user_model().first_name
    image = models.ImageField(upload_to='profile_photo/',null=True)
    phone = models.IntegerField(blank=True,null=True)
    mobile = models.IntegerField(blank=True,null=True)
    age = models.PositiveIntegerField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)

class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(blank=True,null=True)
    subject = models.TextField(blank=True,null=True)
    message = models.TextField(blank=True,null=True)


