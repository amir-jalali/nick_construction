from django.contrib import admin
from .models import Order, Cancellation


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'area', 'total_price', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__phone', 'project__name')


@admin.register(Cancellation)
class CancellationAdmin(admin.ModelAdmin):
    list_display = ('order', 'total_refund', 'penalty', 'created_at')