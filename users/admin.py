from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('phone', 'get_full_name', 'national_code', 'credit', 'is_verified', 'created_at')
    list_filter = ('is_verified', 'is_active')
    search_fields = ('phone', 'first_name', 'last_name', 'national_code')
    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات اضافه', {'fields': ('phone', 'national_code', 'referrer', 'credit', 'address', 'birth_date', 'profile_image', 'is_verified')}),
    )