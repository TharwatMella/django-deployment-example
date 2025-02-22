from django.db import models

# Create your models here.

class NameModel(models.Model):
    name_field=models.TextField(max_length=20)
    def __str__(self):
        return self.name_field
    