from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import File, Version


@receiver(post_save, sender=File)
def file_uploaded(sender, instance, **kwargs):
    Version.objects.create(
        version=instance.actual_version,
        file=instance.file,
        status=instance.status,
        actual_file=instance,
        update_time=instance.update_time,
        user=instance._user
    )
