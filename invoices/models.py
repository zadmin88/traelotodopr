from django.db import models
# from traelotodopr.clients.models import Client
# from inventory.models import Item
from django.contrib.auth.models import User


class Payments(models.Model):
    date   = models.DateField(auto_now=True)
    amount = models.IntegerField()

class Invoice(models.Model):
    client    = models.ForeignKey('clients.Client', related_name='factura', on_delete=models.SET_NULL, null=True)
    item      = models.ForeignKey('inventory.Item', related_name='factura', on_delete=models.SET_NULL, null=True)
    date      = models.DateField(auto_now=True)
    Quantity  = models.IntegerField()
    total     = models.IntegerField()
    debt      = models.IntegerField()
    payments  = models.ForeignKey(Payments, on_delete=models.CASCADE)










# Create your models here.
