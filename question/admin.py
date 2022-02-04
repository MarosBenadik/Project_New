from django.contrib import admin
from .models import Question, Topic, Message

admin.site.register(Question)
admin.site.register(Topic)
admin.site.register(Message)

# Register your models here.
