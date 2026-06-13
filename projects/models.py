from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام پروژه')
    location = models.CharField(max_length=255, verbose_name='موقعیت')
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='فیزیک پروژه (متراژ کل)')
    price_per_meter = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='قیمت هر متر')
    total_capital = models.DecimalField(max_digits=20, decimal_places=0, verbose_name='سرمایه کل')
    predicted_profit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='پیش بینی سود (%)')
    start_date = models.DateField(verbose_name='تاریخ شروع')
    predicted_end_date = models.DateField(verbose_name='پیش بینی تاریخ خاتمه')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه‌ها'

    def __str__(self):
        return self.name


class ProjectProgress(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='progress', verbose_name='پروژه')
    date = models.DateField(verbose_name='تاریخ')
    predicted = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='پیش بینی (%)')
    actual = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='واقعی (%)')

    class Meta:
        verbose_name = 'پیشرفت پروژه'
        verbose_name_plural = 'پیشرفت پروژه‌ها'

    def __str__(self):
        return f"{self.project.name} - {self.date}"


class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='media', verbose_name='پروژه')
    image = models.ImageField(upload_to='projects/', verbose_name='تصویر')
    caption = models.CharField(max_length=255, blank=True, null=True, verbose_name='توضیح')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'تصویر پروژه'
        verbose_name_plural = 'تصاویر پروژه‌ها'


class ProjectNote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='notes', verbose_name='پروژه')
    text = models.TextField(verbose_name='نکته')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'نکته پروژه'
        verbose_name_plural = 'نکات پروژه‌ها'