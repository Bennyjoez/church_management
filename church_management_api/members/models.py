from django.db import models

from districts.models import District
from church_groups.models import ChurchGroup

# Create your models here.
class Member(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
    first_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=True)
    nick_name = models.CharField(max_length=200, blank=True) # Like Mama Maina
    address = models.CharField(max_length=200) 
    phone_number = models.CharField(max_length=20, unique=True)
    join_date = models.DateField(auto_now_add=True)
    district = models.ForeignKey(District, blank=True, null=True, on_delete=models.CASCADE)
    church_group = models.ForeignKey(ChurchGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"