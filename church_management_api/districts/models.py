from django.db import models

# Create your models here.
class District(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    boundaries = models.TextField(blank=True)


    def __str__(self):
        return f"{self.name}"