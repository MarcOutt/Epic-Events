from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'role')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'role', 'is_admin', 'is_staff'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ()


admin.site.register(CustomUser, CustomUserAdmin)
