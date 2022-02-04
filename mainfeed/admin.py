from django.contrib import admin
from .models import Post, Comment, Notification, Tag

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(Tag)
