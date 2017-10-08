from django.db import models

# Create your models here.

class Project(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    STATUS_PROJECT_CHOICES = (
        ('0','Creado'),
        ('1','Planificado'),
        ('2','Gestión por iniciar),
        ('3','En ejecución'),
        ('4','Finalizado'),
        ('5','Detenido'),
        ('6','Cancelado'),
    )
    status = models.CharField(max_length = 1, choices = STATUS_PROJECT_CHOICES)
    location = models.TextField(blank = True, null = True)
    PROJECT_TYPE_CHOICES = (
        ('0','Interno'),
        ('1','Externo'),
        ('2','Conjunto'),
    )
    project_type = models.CharField(max_length = 1, choices = PROJECT_TYPE_CHOICES)
    attendant = CharField(max_length = 45, blank = True, null = True)
    snip = CharField(max_length = 45, blank = True, null = True)
    nog = CharField(max_length = 45, blank = True, null = True)
    smip = CharField(max_length = 45, blank = True, null = True)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    Budget_id = models.ForeignKey('Bugdet', blank = True, null = True)
    User_id = models.ForeignKey('Users.User')



    def __str__(self):
        return str(self.name + self.status + self.attendant)

class Budget(models.Model):
    id = models.AutoField(primary_key = True)
    amout = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0)])
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.amout)

class Entry(models.Model):
    id = models.AutoField(primary_key = True)
    description = models.CharField(max_length=45)
    quantity = models.FloatField()
    unity = models.CharField(max_length=45)
    unit_cost = models.FloatField()
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    Budget_id = models.ForeignKey('Bugdet')

    def __str__(self):
        return str(self.description + self.quantity)
