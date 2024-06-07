from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name
