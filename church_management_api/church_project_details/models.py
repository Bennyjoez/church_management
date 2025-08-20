from django.db import models

from church_projects.models import ChurchProject

# Create your models here.
class ChurchProjectDetail(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(ChurchProject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
