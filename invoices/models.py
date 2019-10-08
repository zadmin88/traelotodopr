from django.db import models
from django.contrib.auth.models import User


class Invoice(models.Model):
    client    = models.ForeignKey('clients.Client', related_name='factura', on_delete=models.CASCADE, null=True)
    item      = models.ForeignKey('inventory.Item', related_name='factura', on_delete=models.CASCADE, null=True)
    date      = models.DateField(auto_now=True)
    Quantity  = models.IntegerField()
    total     = models.IntegerField()
    debt      = models.IntegerField(null=True)

    # user      = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        return '%s - %s' % ( self.id , self.client)


class Payments(models.Model):
    date   = models.DateField(auto_now=True)
    amount = models.IntegerField()
    invoice  = models.ForeignKey(Invoice, on_delete=models.CASCADE,null=True)







# Create your models here.
