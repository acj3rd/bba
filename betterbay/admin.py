from django.contrib import admin

# Register your models here.

from .models import Event, EventType, News

admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(News)
