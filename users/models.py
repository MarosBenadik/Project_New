from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import secrets
from .utils import custom_id


def getcurrentusername(instance, filename):
    return "uploads/profilepictures/{0}/{1}".format(instance.user.username, filename)

def getcurrentbusiness(instance, filename):
    return "uploads/businesspictures/{0}/{1}".format(instance.business_name, filename)

def getcurrentuser(instance, filename):
    return "uploads/userpictures/{0}/{1}".format(instance, filename)


class ServiceCategory(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__ (self):
        return self.name

class FeedBack(models.Model):
    class Rating(models.TextChoices):
        very_good = '1', "Velmy spokojny"
        good = '2', "Spokojny"
        none = '3', "Nemam Nazor"
        bad = '4', "Nie Velmy Spokojny"
        very_bad = '5', "Nespokojny"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=250, blank=True, null=True)
    rating = models.CharField(max_length=15, choices=Rating.choices)
    created_on = models.DateTimeField(auto_now_add=True)


class SubServices(models.Model):
    class Gender(models.TextChoices):
        male = '1', "Sluzba pre Muzov"
        female = '2', "Sluzba pre zeny"
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=15, choices=Gender.choices)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    length = models.DecimalField(max_digits=3, decimal_places=2, blank=True)
    feedback = models.ManyToManyField(FeedBack, blank=True, null=True)


class Service(models.Model):
    category = models.ManyToManyField(ServiceCategory, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    service = models.ManyToManyField(SubServices, blank=True, null=True)


    def __str__ (self):
        return self.name


class Adress(models.Model):
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField (max_length=35, blank=True, null=True)
    postcode = models.CharField (max_length=30, blank=True, null=True)


class WorkingDays(models.Model):
    class Days(models.TextChoices):
        monday = '1', "Pondelok"
        tuesday = '2', "Utorok"
        wednesday = '3', "Streda"
        thursday = '4', "Stvrtok"
        friday = '5', "Piatok"
        saturday = '6', "Sobota"
        sunday = '7', "Nedela"
    day = models.CharField(max_length=15, choices=Days.choices)
    start = models.TimeField(blank=True)
    end = models.TimeField(blank=True)
    day_off = models.BooleanField(default=False)

class Business(models.Model):
    business_id = models.IntegerField(primary_key=True, verbose_name='business')
    business_name = models.CharField (max_length=30, blank=True, default='Unknown')
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.ForeignKey(Adress, on_delete=models.CASCADE, blank=True, null=True)
    working_days = models.ManyToManyField(WorkingDays, blank=True)
    services = models.ManyToManyField(Service, blank=True, null=True)
    profilepicture = models.ImageField(upload_to=getcurrentbusiness, default='uploads/profilepictures/default.png',
                                        blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name='businessfollowers')
    business_number = models.IntegerField(null=True)



class Image(models.Model):
    image = models.ImageField(upload_to=getcurrentuser, default='uploads/profilepictures/default.png', blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):

    user = models.ForeignKey(User, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, default='Unknown')
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    profilepicture = models.ImageField(upload_to=getcurrentusername, default='uploads/profilepictures/default.png', blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    followings = models.ManyToManyField(User, blank=True, related_name='followings')
    images = models.ManyToManyField(Image, blank=True, null=True)
    bussiness = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True)