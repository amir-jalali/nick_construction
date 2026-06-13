from django.db import models
from django.conf import settings


class Order(models.Model):
    STATUS_CHOICES = [
        ('active', 'فعال'),
        ('cancelled', 'انصراف داده'),
        ('sold', 'فروخته شده'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='کاربر'
    )
    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='پروژه'
    )
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='متراژ خریداری شده')
    price_per_meter = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='قیمت هر متر در زمان خرید')
    total_price = models.DecimalField(max_digits=20, decimal_places=0, verbose_name='مبلغ کل خرید')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ خرید')

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش‌ها'

    def __str__(self):
        return f"{self.user} - {self.project} - {self.area}m²"

    @property
    def current_value(self):
        return self.area * self.project.price_per_meter

    @property
    def profit(self):
        return self.current_value - self.total_price


class Cancellation(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='cancellation', verbose_name='سفارش')
    cancel_price_per_meter = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='قیمت هر متر در زمان انصراف')
    total_refund = models.DecimalField(max_digits=20, decimal_places=0, verbose_name='مبلغ بازگشتی')
    penalty = models.DecimalField(max_digits=20, decimal_places=0, verbose_name='کسر کارمزد (0.5%)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انصراف')

    class Meta:
        verbose_name = 'انصراف'
        verbose_name_plural = 'انصراف‌ها'

    def __str__(self):
        return f"انصراف - {self.order}"