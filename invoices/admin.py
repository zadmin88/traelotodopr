from django.contrib import admin
from .models import Invoice, Payments

admin.site.register(Invoice)
admin.site.register(Payments)
