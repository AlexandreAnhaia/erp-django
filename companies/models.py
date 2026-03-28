from django.db import models


# Create your models here.
class Enterprise(models.Model):
    name = models.CharField(max_length=175)
    user = models.ForeignKey("accounts.user", on_delete=models.CASCADE)