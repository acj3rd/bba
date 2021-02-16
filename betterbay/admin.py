from django.contrib import admin

# Register your models here.

from .models import Event, EventType

admin.site.register(Event)
admin.site.register(EventType)
