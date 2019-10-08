from django.shortcuts import render
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
from .models import Client
from invoices.models import Invoice

class CreateClient(LoginRequiredMixin, generic.CreateView):
    model = Client
    fields = [ 'name',
               'phone',
               'mail',
               'address'
     ]
    template_name = 'clients/create_client.html'
    success_url = reverse_lazy('list_clients')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateClient, self).form_valid(form)
        return redirect('list_clients')

@login_required
def detail_client(request, pk):
    client = Client.objects.get(pk=pk)
    invoices= Invoice.objects.filter(client=client)
    return render(request, 'clients/detail_client.html', {'client':client, 'invoices':invoices})

class DetailList(LoginRequiredMixin, generic.ListView):
    model = Client
    template_name = 'clients/list_clients.html'


class UpdateClient(LoginRequiredMixin, generic.UpdateView):
    model = Client
    template_name = 'clients/update_client.html'
    fields = [ 'name',
               'phone',
               'mail',
               'address'
     ]
    success_url = reverse_lazy('list_clients')

    def get_object(self):
        client = super(UpdateClient, self).get_object()
        if not client.user == self.request.user:
            raise Http404
        return client

class DeleteClient(LoginRequiredMixin, generic.DeleteView):
    model = Client
    template_name = 'clients/delete_client.html'
    success_url = reverse_lazy('list_clients')

    def get_object(self):
        client = super(DeleteClient, self).get_object()
        if not client.user == self.request.user:
            raise Http404
        return client
