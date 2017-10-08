from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=60, blank = False, null = False)
    attendant = models.CharField(max_length=45, blank = False, null = False)
    STATUS_PROJECT_CHOICES = (
        ('0','Entregado'),
        ('1','En revision'),
        ('2','Finalizado'),
    )
    status = models.CharField(max_length = 1, choices=STATUS_PROJECT_CHOICES)
    project = models.ForeignKey('projects.Project')
    budget = models.ForeignKey('budgets.Budget')
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.name


def path_document(instance, filename):
    return "reports/{0}/{1}/{2}".format(
        instance.item.create_time,
        instance.item.id,
        instance.item.name,
    )


class File(models.Model):
    id = models.AutoField(primary_key = True)
    file = models.FileField(upload_to = path_document)
    create_time = models.DateField(auto_now_add = True)
    item = models.ForeignKey('items.Item')

    def __unicode__(self):
        return self.file
