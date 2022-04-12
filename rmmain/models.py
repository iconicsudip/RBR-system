
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,blank=False)
    email = models.CharField(max_length=200,blank=False)
    def __str__(self):
        return str(self.username)

class Manager(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,blank=False)
    email = models.CharField(max_length=200,blank=False)
    pnumber = models.CharField(max_length=11,blank=False)
    def __str__(self):
        return str(self.username)
class Roomtype(models.Model):
    roomtype = models.CharField(max_length=200,blank=False)
    def __str__(self):
        return str(self.roomtype)
class Location(models.Model):
    city = models.CharField(max_length=200,blank=False)
    state = models.CharField(max_length=200,blank=False)
    country = models.CharField(max_length=200,blank=False)
    def __str__(self):
        return str(self.city)
class Room(models.Model):
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)
    roomtype = models.ForeignKey(Roomtype,on_delete=models.CASCADE)
    capacity = models.IntegerField(default=0,blank=False)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=10000,blank=False)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    address = models.CharField(max_length=10000,blank=False)
    mnumber = models.CharField(max_length=11,blank=False)
    def __str__(self):
        s = "{}".format(self.id)
        return s
    
class Slotdelay(models.Model):
    manager = models.OneToOneField(Manager,on_delete=models.CASCADE)
    slotrange = models.IntegerField(default=1)
    bookbefore = models.IntegerField(default=1)
    def __str__(self):
        return f"[ {self.manager} {self.slotrange} {self.bookbefore} ]"
    
class Timing(models.Model):
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)
    roomid = models.ForeignKey(Room,on_delete=models.CASCADE)
    smonday = models.TimeField(default= "09:00:00" ,blank=True)
    emonday = models.TimeField(default= "21:00:00",blank=True)
    stuesday = models.TimeField(default= "09:00:00",blank=True)
    etuesday = models.TimeField(default= "21:00:00",blank=True)
    swednesday = models.TimeField(default= "09:00:00",blank=True)
    ewednesday = models.TimeField(default= "21:00:00",blank=True)
    sthursday = models.TimeField(default= "09:00:00",blank=True)
    ethursday = models.TimeField(default= "21:00:00",blank=True)
    sfriday = models.TimeField(default= "09:00:00",blank=True)
    efriday = models.TimeField(default= "21:00:00",blank=True)
    ssaturday = models.TimeField(default= "09:00:00",blank=True)
    esaturday = models.TimeField(default= "21:00:00",blank=True)
    ssunday = models.TimeField(default= "09:00:00",blank=True)
    esunday = models.TimeField(default= "21:00:00",blank=True)
    def __str__(self):
        return f"[ {self.manager} {self.roomid} ]"
    

# Create your models here.
