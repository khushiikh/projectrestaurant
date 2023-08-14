from django.db import models

# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Phone=models.IntegerField()
    Message=models.TextField()


