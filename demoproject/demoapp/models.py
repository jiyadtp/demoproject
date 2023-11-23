from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class EmployeeDetails(models.Model):
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, db_index=True)
    name = models.CharField(max_length=100, null=True, db_index=True)
    phone = models.CharField(max_length=20, null=True, db_index=True)
    email = models.CharField(max_length=100, null=True, db_index=True)
    age = models.CharField(max_length=100, null=True, db_index=True)
