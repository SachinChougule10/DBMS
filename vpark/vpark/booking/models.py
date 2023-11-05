from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Location(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    location_name = models.CharField(max_length=500,unique=True)
    image = models.ImageField(upload_to='location_image/',null=True)
    location_address = models.TextField()
    location_link = models.CharField(max_length=800,null=True)
    four_space = models.IntegerField()
    two_space = models.IntegerField()
    three_space = models.IntegerField()
    mobile = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.location_name


class Book(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=200)
    vehicle_no = models.CharField(max_length=200,blank=True,null=True)
    date = models.DateField(default=datetime.date.today,blank=True,null=True)
    start_time = models.TimeField(default=datetime.datetime.now().strftime("%H:%M:%S"))
    end_time = models.TimeField(default=datetime.datetime.now().strftime("%H:%M:%S"))
    price = models.IntegerField(null=True)
    slots = models.IntegerField()

    def __str__(self):
        return self.user