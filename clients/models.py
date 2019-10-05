from django.db import models
from django.contrib.auth.models import User
# from traelotodopr.inventory.models import Item
# from traelotodopr.invoices.models  import Invoice

class Client(models.Model):
    name    = models.CharField(max_length=255)
    phone   = models.CharField(max_length=255)
    mail    = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    items   = models.ManyToManyField('inventory.Item', through='invoices.Invoice', related_name='invoices')

    def __str__(self):
        return '%s' % self.name
