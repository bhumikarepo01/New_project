from django.contrib import admin
from .models import Event, Attendee


class AttendeeInline(admin.TabularInline):
    model = Attendee
    extra = 1


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'capacity']
    inlines = [AttendeeInline]


admin.site.register(Event, EventAdmin)
admin.site.register(Attendee)