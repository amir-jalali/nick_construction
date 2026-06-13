from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل')
    national_code = models.CharField(max_length=10, unique=True, verbose_name='کد ملی')
    referrer = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='referrals',
        verbose_name='معرف'
    )
    credit = models.DecimalField(
        max_digits=15,
        decimal_places=0,
        default=0,
        verbose_name='اعتبار'
    )
    address = models.TextField(blank=True, null=True, verbose_name='آدرس')
    birth_date = models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')
    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True,
        verbose_name='تصویر پروفایل'
    )
    is_verified = models.BooleanField(default=False, verbose_name='تأیید شده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name='user permissions'
    )

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'national_code']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return f"{self.get_full_name()} - {self.phone}"