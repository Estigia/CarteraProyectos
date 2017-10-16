import uuid
from django.db import models


class Budget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=65, null=False)
    amount = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)


class Project(models.Model):
    PROJECT_TYPE_CHOICES = (
        ('0', 'Interno'),
        ('1', 'Externo'),
        ('2', 'Conjunto'),
    )
    STATUS_PROJECT_CHOICES = (
        ('0', 'Creado'),
        ('1', 'Planificado'),
        ('2', 'Gestión por iniciar'),
        ('3', 'En ejecución'),
        ('4', 'Finalizado'),
        ('5', 'Detenido'),
        ('6', 'Cancelado'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=1,
        choices=STATUS_PROJECT_CHOICES,
        default='0'
    )
    location = models.TextField(blank=True, null=True)
    project_type = models.CharField(
        max_length=1,
        choices=PROJECT_TYPE_CHOICES,
        default='0'
    )
    attendant = models.CharField(max_length=45, blank=True, null=True)
    snip = models.CharField(max_length=45, blank=True, null=True)
    nog = models.CharField(max_length=45, blank=True, null=True)
    smip = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    budget = models.ForeignKey('Budget')
    # user = models.ForeignKey('users.User')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_time']


class Entry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    description = models.CharField(max_length=45)
    quantity = models.FloatField()
    unity = models.CharField(max_length=45)
    unit_cost = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    budget = models.ForeignKey('Budget')

    def __str__(self):
        return self.description
