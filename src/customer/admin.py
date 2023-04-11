from customer.models import Customer
from django.contrib import admin


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created',
                    'date_update', 'sales_contact')
    list_filter = ('company_name', 'date_created')
    search_fields = ('first_name', 'last_name', 'email', 'company_name', 'sales_contact__username')
    ordering = ('-date_created',)

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'mobile')
        }),
        ('Company Information', {
            'fields': ('company_name',)
        }),
        ('Sales Contact', {
            'fields': ('sales_contact',)
        })
    )


admin.site.register(Customer, CustomerAdmin)