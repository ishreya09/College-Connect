from django.db import models

# Create your models here.
class Department(models.Model):
    department_name= models.CharField(max_length=500,null=True, blank= True)
    department_id= models.CharField()