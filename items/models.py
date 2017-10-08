from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=60, blank = False, null = False)
    attendant = models.CharField(max_length=45, blank = False, null = False)
    STATUS_PROJECT_CHOICES = (
        ('0','Creado'),
        ('1','Planificado'),
        ('2','Gestión por iniciar),
        ('3','En ejecución'),
        ('4','Finalizado'),
        ('5','Detenido'),
        ('6','Cancelado'),
    )
    status = models.CharField(max_length = 1, choices=STATUS_PROJECT_CHOICES)
    project = models.ForeignKey('Proyecto.proyecto')
    budget = models.ForeignKey('Presupuesto.presupuesto')

    def __unicode__(self):
        return str(self.id)


class File(models.Model):
    id = models.AutoField(primary_key = True)
    file = models.FileField(upload_to='upload_to /%Y /%m /%d/')
    date = models.DateField(auto_now = False)
    item = models.ForeignKey('items.Item')

    def __unicode__(self):
        return str(self.id)





        
