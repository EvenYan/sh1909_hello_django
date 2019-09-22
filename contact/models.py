from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=11)

    def __str__(self):
        return self.name
