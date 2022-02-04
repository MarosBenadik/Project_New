from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import secrets
from .utils import custom_id



def getcurrentusername(instance, filename):
    return "uploads/profilepictures/{0}/{1}".format(instance.user.username, filename)


class ServiceCategory(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__ (self):
        return self.name

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    service = models.CharField(max_length=150, blank=True, null=True)
    length = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__ (self):
        return self.name


class Adress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    street = models.CharField (max_length=50, blank=True, null=True)
    city = models.CharField (max_length=35, blank=True, null=True)
    postcode = models.CharField (max_length=30, blank=True, null=True)



class WorkingDays(models.Model):
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField (default=False)
    wednesday = models.BooleanField (default=False)
    thursday = models.BooleanField (default=False)
    friday = models.BooleanField (default=False)
    saturday = models.BooleanField (default=False)
    sunday = models.BooleanField (default=False)



class BusinessProfile(models.Model):
    businessuser = models.OneToOneField(User, primary_key=True, verbose_name='business', related_name='businessprofile', on_delete=models.CASCADE)
    business_name = models.CharField (max_length=30, blank=True, default='Unknown')
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.OneToOneField(Adress, on_delete=models.CASCADE, blank=True, null=True)
    working_days = models.ManyToManyField(WorkingDays, blank=True)
    profilepicture = models.ImageField (upload_to=getcurrentusername, default='uploads/profilepictures/default.png',
                                        blank=True)
    followers = models.ManyToManyField (User, blank=True, related_name='businessfollowers')
    business_number = models.IntegerField(null=True)



class FreelanceProfile(models.Model):

    freelanceuser = models.OneToOneField(User, primary_key=True, verbose_name='freelance', related_name='freelanceprofile', on_delete=models.CASCADE)
    name = models.CharField (max_length=30, blank=True, default='Unknown')
    bio = models.TextField (max_length=500, blank=True, null=True)
    birth_date = models.DateField (blank=True, null=True)
    location = models.OneToOneField(Adress, on_delete=models.CASCADE, blank=True, null=True)
    profilepicture = models.ImageField(upload_to=getcurrentusername, default='uploads/profilepictures/default.png',
                                        blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name='freelancefollowers')



class UserProfile(models.Model):

    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, default='Unknown')
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    profilepicture = models.ImageField(upload_to=getcurrentusername, default='uploads/profilepictures/default.png', blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')