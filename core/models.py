from django.db import models
from django.contrib.sites.models import Site


class SiteProfile(models.Model):
    title = models.CharField(verbose_name="عنوان سایت", max_length=60)
    description = models.CharField(verbose_name="توضیحات سایت", max_length=255)
    site = models.OneToOneField(Site, on_delete=models.SET_NULL, null=True,
                                verbose_name="وب سایت", )


class TimeStampModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(verbose_name="زمان ایجاد", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="زمان بروزرسانی", auto_now=True)
