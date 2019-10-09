from django.contrib import admin
from .models import Invoice, Payments, Shipments

admin.site.register(Invoice)
admin.site.register(Payments)
admin.site.register(Shipments)
