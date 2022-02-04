from django.contrib import admin
from .models import UserProfile, BusinessProfile, FreelanceProfile, WorkingDays, Adress, Service, ServiceCategory

admin.site.register(UserProfile)
admin.site.register(BusinessProfile)
admin.site.register(FreelanceProfile)
admin.site.register(WorkingDays)
admin.site.register(Adress)
admin.site.register(Service)
admin.site.register(ServiceCategory)