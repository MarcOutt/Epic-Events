from django.contrib import admin
from event.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'customer', 'contract', 'date_created', 'date_update', 'support_contact', 'event_ended', 'attendees',
        'event_date')
    list_filter = ('event_ended', 'event_date', 'support_contact')
    search_fields = ('customer__name', 'contract__name', 'support_contact__last_name')
    date_hierarchy = 'event_date'
    fieldsets = (
        (None, {
            'fields': ('customer', 'contract', 'event_date', 'attendees')
        }),
        ('Event Details', {
            'fields': ('notes', 'event_ended', 'support_contact')
        }),
    )


admin.site.register(Event, EventAdmin)
