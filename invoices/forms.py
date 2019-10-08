from .models          import Invoice, Payments
from clients.models   import Client
from inventory.models import Item
from django           import forms



class InvoiceForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(),
                                    empty_label="Seleccionar Cliente")

    item = forms.ModelChoiceField(queryset=Item.objects.all(),
                                    empty_label="Seleccionar Producto")

    total = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}) )

    abono = forms.IntegerField(required=False)

    class Meta:
        model  = Invoice
        fields = [      'client',
                        'item',
                        'Quantity',
                        'total',
                        'abono'


         ]
        labels = {  'client': 'Cliente',
                    'item':'Producto',
                    'Quantity':'Cantidad',
                    'total':'Total' }

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = [ 'amount' ]
        labels  =  {'amount': 'Pago'}
