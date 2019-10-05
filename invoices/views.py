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
from .forms  import InvoiceForm#

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

            return redirect('create_invoice')
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
    model = Invoice
    template_name = 'invoices/list_invoices.html'

class DetailInvoice(LoginRequiredMixin, generic.DetailView):
    model = Invoice
    template_name = 'invoices/detail_invoice.html'

# @login_required
# def add_video(request, pk):
#     # VideoFormSet = formset_factory(VideoForm, extra=5)
#     form        = VideoForm()
#     search_form = SearchForm()
#     hall        = Hall.objects.get(pk=pk)
#
#     if not hall.user == request.user:
#         raise Http404
#
#     if request.method == 'POST':
#         #create
#         form = VideoForm(request.POST)
#         if form.is_valid():
#             video            = Video()
#             video.url        = form.cleaned_data['url']
#             parsed_url       = urllib.parse.urlparse(video.url)
#             video_id         = urllib.parse.parse_qs(parsed_url.query).get('v')
#             if video_id:
#                 video.youtube_id = video_id[0]
#                 response         = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={ video_id[0] }&key={ YOUTUBE_API_KEY}')
#                 jason            = response.json()
#                 tittle           = jason['items'][0]['snippet']['title']
#                 video.tittle     = tittle
#                 video.hall       = hall
#                 video.save()
#                 return redirect('detail_hall', pk)
#             else:
#                 errors = form._errors.setdefault('url',ErrorList())
#                 errors.append('Needs to be a youtube Url')
#
#     return render(request, 'halls/add_video.html', {'form':form, 'search_form':search_form, 'hall':hall})
