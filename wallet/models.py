from django.db import models
from django.conf import settings


class Transaction(models.Model):
    TYPE_CHOICES = [
        ('deposit', 'واریز'),
        ('withdraw', 'برداشت'),
        ('referral_credit', 'اعتبار معرف'),
        ('purchase', 'خرید'),
        ('cancellation_refund', 'استرداد انصراف'),
        ('cancellation_penalty', 'کسر کارمزد انصراف'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions',
        verbose_name='کاربر'
    )
    transaction_type = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES,
        verbose_name='نوع تراکنش'
    )
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=0,
        verbose_name='مبلغ'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='توضیحات'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ'
    )

    class Meta:
        verbose_name = 'تراکنش'
        verbose_name_plural = 'تراکنش‌ها'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} - {self.transaction_type} - {self.amount}"