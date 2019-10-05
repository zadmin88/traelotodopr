from django.db import models
from django.contrib.auth.models import User

DEFAULT_ID = 1

class Item(models.Model):
    name     = models.CharField(max_length=255)
    desc     = models.CharField(max_length=255)
    price    = models.IntegerField()
    cost     = models.IntegerField()
    quantity = models.IntegerField()
    user     = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        return '%s' % self.name
