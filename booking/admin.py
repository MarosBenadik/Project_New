from django.contrib import admin
from booking.models import event, event_abstract
from . import models


@admin.register(models.event.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.event.Event
    list_display = [
        "id",
        "title",
        "user",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title"]



# Register your models here.
