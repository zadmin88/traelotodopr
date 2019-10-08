from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# from .forms import VideoForm, SearchForm
from django.forms import formset_factory
from django.http import Http404, JsonResponse
from django.forms.utils import ErrorList
import urllib
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Invoice, Payments
from inventory.models import Item
from clients.models import Client
from .forms  import InvoiceForm, PaymentsForm
import pdb
from django.db.models import Sum

@login_required
def create_invoice(request):
    form        = InvoiceForm()
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice          = Invoice()
            client           = Client.objects.get(pk=request.POST['client'])
            item             = Item.objects.get(pk=request.POST['item'])
            invoice.client   = client
            invoice.item     = item
            invoice.Quantity = form.cleaned_data['Quantity']
            if item.quantity >= invoice.Quantity:
                invoice.total    = form.cleaned_data['total']
                invoice.debt     = form.cleaned_data['total']
                invoice.save()
                item.quantity    = int(item.quantity) - int(invoice.Quantity)
                item.save()
                if form.cleaned_data['abono']:
                    payment = Payments()
                    payment.amount = form.cleaned_data['abono']
                    payment.invoice = invoice
                    payment.save()
                    invoice.debt = int(invoice.debt) - int(payment.amount)
                    invoice.save()
                return redirect('list_invoices')
            else:
                errors = form._errors.setdefault('Quantity', ErrorList())
                errors.append('Cantidad disponible:'+str(item.quantity))

    return render(request, 'invoices/create_invoice.html', {'form':form})



@login_required
def update_total(request):
    if request.method == 'POST':
        item  = Item.objects.get(pk = request.POST['item_pk'] )
        val   = int(request.POST['quantity'])
        price = int(item.price)
        total = price * val
        return JsonResponse({'total': total})
    # return JsonResponse({'total': total})

class InvoicesList(LoginRequiredMixin, generic.ListView):
    model         = Invoice
    template_name = 'invoices/list_invoices.html'

class DetailInvoice(LoginRequiredMixin, generic.DetailView):
    model         = Invoice
    template_name = 'invoices/detail_invoice.html'

class DeleteInvoice(LoginRequiredMixin, generic.DeleteView):
    model         = Invoice
    template_name = 'invoices/delete_invoice.html'
    success_url   = reverse_lazy('list_invoices')

    # def get_object(self):
    #     item = super(DeleteItem, self).get_object()
    #     if not item.user == self.request.user:
    #         raise Http404
    #     return item

def detail_invoice(request, pk):
    form          = PaymentsForm()
    invoice       = Invoice.objects.get(pk=pk)
    payments      = Payments.objects.filter(invoice=pk)
    payment_total = Payments.objects.filter(invoice=pk).aggregate(Sum('amount'))

    if request.method == 'POST':
        form            = PaymentsForm(request.POST)
        if form.is_valid():
            payment         = Payments()
            payment.amount  = form.cleaned_data['amount']
            payment.invoice = invoice
            payment.save()
            invoice.debt = int(invoice.debt) - int(payment.amount)
            invoice.save()
            return redirect('detail_invoice', pk)

    return render(request, 'invoices/detail_invoice.html', {'invoice':invoice, 'payments':payments, 'form': form,'payment_total':payment_total})
