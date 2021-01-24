from django.db import models
from django.conf import settings


def upload_status_image(instance, filename):
    return f'updates/{instance.user}/{filename}'


class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_status_image, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]


    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'
