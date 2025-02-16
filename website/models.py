from django.db import models

# Create your models here.
class Record(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")