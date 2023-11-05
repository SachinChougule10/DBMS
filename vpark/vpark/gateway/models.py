from django.db import models
from django.contrib.auth.models import User
import datetime
from booking.models import Location
# Create your models here.


class Entry(models.Model):
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True)
    vehicle_no = models.CharField(max_length=200)
    vehicle_type = models.CharField(max_length=300)
    mobile = models.IntegerField()
    tag_number = models.CharField(max_length=10,null=True)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=datetime.datetime.now().strftime("%H:%M:%S"))



