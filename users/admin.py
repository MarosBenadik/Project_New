from django.contrib import admin
from .models import UserProfile, WorkingDays, SubServices, FeedBack, Adress, Service, ServiceCategory, Image, Business, WorkingDays, Adress

admin.site.register(UserProfile)
admin.site.register(WorkingDays)
admin.site.register(Adress)
admin.site.register(Service)
admin.site.register(ServiceCategory)
admin.site.register(SubServices)
admin.site.register(Image)
admin.site.register(Business)

admin.site.register(FeedBack)

