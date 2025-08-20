from django.db import models

from church_groups.models import ChurchGroup

# Create your models here.
class ChurchProject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    church_group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
