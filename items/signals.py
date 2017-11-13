from django.db.models.signals import pre_save

from .models import File, Version


@receiver(pre_save, sender=File)
def file_uploaded(sender, instance, **kwargs):
    try:
        old_instance = File.objects.get(pk=instance.id)
        Version.objects.create(
            version=old_instance.actual_version,
            file=old_instance.file,
            status=old_instance.status,
            actual_file=instance,
            update_time=old_instance.update_time
        )
    except:
        Version.objects.create(
            version=instance.actual_version,
            file=instance.file,
            status=instance.status,
            actual_file=instance,
            update_time=instance.update_time
        )
