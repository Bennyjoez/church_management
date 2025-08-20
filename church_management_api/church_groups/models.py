from django.db import models
from churches.models import Church

# Create your models here.
class ChurchGroup(models.Model):
  id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
  church = models.ForeignKey(Church, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=500, blank=True)

  def __str__(self):
    return f"{self.name}"
