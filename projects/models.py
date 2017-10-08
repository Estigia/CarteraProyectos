from django.db import models

# Create your models here.

class Budget(models.Model):
    id = models.AutoField(primary_key = True)
    amount = models.FloatField()
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.amount)

class Project(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    STATUS_PROJECT_CHOICES = (
        ('0','Creado'),
        ('1','Planificado'),
        ('2','Gestión por iniciar'),
        ('3','En ejecución'),
        ('4','Finalizado'),
        ('5','Detenido'),
        ('6','Cancelado'),
    )
    status = models.CharField(max_length = 1, choices = STATUS_PROJECT_CHOICES, default='0')
    location = models.TextField(blank = True, null = True)
    PROJECT_TYPE_CHOICES = (
        ('0','Interno'),
        ('1','Externo'),
        ('2','Conjunto'),
    )
    project_type = models.CharField(max_length = 1, choices = PROJECT_TYPE_CHOICES, default = '0')
    attendant = models.CharField(max_length = 45, blank = True, null = True)
    snip = models.CharField(max_length = 45, blank = True, null = True)
    nog = models.CharField(max_length = 45, blank = True, null = True)
    smip = models.CharField(max_length = 45, blank = True, null = True)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    budget = models.ForeignKey('Budget')
    # user = models.ForeignKey('users.User')

    def __str__(self):
        return str(self.name + self.status + self.attendant)

class Entry(models.Model):
    id = models.AutoField(primary_key = True)
    description = models.CharField(max_length=45)
    quantity = models.FloatField()
    unity = models.CharField(max_length=45)
    unit_cost = models.FloatField()
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    budget = models.ForeignKey('Budget')

    def __str__(self):
        return str(self.description + self.quantity)
