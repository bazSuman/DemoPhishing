from django.db import models

# Create your models here.

class DemoDatabase(models.Model):
    username = models.CharField(max_length=125)
    password = models.CharField(max_length=125)

    def __str__(self):
        return self.username