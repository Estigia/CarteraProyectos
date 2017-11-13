import uuid
from django.db import models
from django.conf import settings


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=60, blank=False, null=False)
    attendant = models.CharField(max_length=45, blank=False, null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


def path_document(instance, filename):
    return "projects/{0}/{1}/{2}/{3}".format(
        instance.project.id,
        instance.item.name.replace(' ','_'),
        instance.item.create_time.date(),
        filename
    )


class File(models.Model):
    STATUS_PROJECT_CHOICES = (
        ('0', 'Entregado'),
        ('1', 'En revision'),
        ('2', 'Finalizado'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    actual_version = models.IntegerField(default=1)
    file = models.FileField(upload_to=path_document, max_length=450)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_PROJECT_CHOICES,
        default='0'
    )
    project = models.ForeignKey('projects.Project', null=True)
    item = models.ForeignKey('Item')

    def __str__(self):
        return self.file.name

    def get_media_path(self):
        return "{}{}".format(settings.MEDIA_URL, self.file)


class Version(models.Model):
    STATUS_PROJECT_CHOICES = (
        ('0', 'Entregado'),
        ('1', 'En revision'),
        ('2', 'Finalizado'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    version = models.IntegerField()
    file = models.CharField(max_length=450)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField()
    status = models.CharField(
        max_length=1,
        choices=STATUS_PROJECT_CHOICES,
        default='0'
    )
    actual_file = models.ForeignKey('File')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.file.name

    def get_media_path(self):
        return "{}{}".format(settings.MEDIA_URL, self.file)

    class Meta:
        ordering = ['-update_time']
