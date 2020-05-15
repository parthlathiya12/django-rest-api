from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=250)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
