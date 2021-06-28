from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=254, unique=True)
    isSubscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.email
