from django.db import models

# Create your models here.
class Church(models.Model):
  id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
  name = models.CharField(max_length=50)
  parish = models.CharField(max_length=50)
  description = models.TextField(max_length=500, blank=True)
  address = models.CharField(max_length=200, blank=False)
  latitude = models.FloatField(blank=False)
  longitude = models.FloatField(blank=False)

  def __str__(self):
    return f"{self.name}"