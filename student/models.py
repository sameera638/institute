from django.db import models
from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=20)
    roll_no=models.IntegerField(max_length=5)
    mobile=models.CharField(max_length=10)

    

# Create your models here.

  