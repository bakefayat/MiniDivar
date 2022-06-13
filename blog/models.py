from tabnanny import verbose
from django.db import models


# Create your models here.
class Articles(models.Model):
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['id', ]
        
    title = models.CharField(max_length=80, verbose_name="عنوان")
    description = models.TextField(max_length=200, verbose_name="توضیحات")
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name="نامک")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
