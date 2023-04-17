from contract.models import Contract
from django.contrib import admin


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'sales_contact', 'customer', 'date_created', 'date_update', 'status', 'amount',
                    'payment_due')
    list_filter = ('customer', 'sales_contact', 'date_created')
    search_fields = ('customer', 'status', 'sales_contact')
    ordering = ('-date_created',)

    fieldsets = (
        ('Company Information', {
            'fields': ('customer',)
        }),
        ('Contract Information', {
            'fields': ('sales_contact', 'status', 'amount', 'payment_due')
        }),
    )


admin.site.register(Contract, ContractAdmin)
