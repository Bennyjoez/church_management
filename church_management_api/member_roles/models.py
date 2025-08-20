from django.db import models
from members.models import Member
from districts.models import District

# Create your models here.
class MemberRoles(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
    member = models.ForeignKey(Member, blank=False, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, blank=False)
    district = models.ForeignKey(District, blank=False, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()

    def __str__(self):
        return f"{self.member} {self.role}"