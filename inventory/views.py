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
from .models import Item

class CreateItem(LoginRequiredMixin, generic.CreateView):
    model = Item
    fields = [  'name',
                'desc',
                'price',
                'cost',
                'quantity'
     ]
    template_name = 'inventory/create_item.html'
    success_url = reverse_lazy('list_items')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateItem, self).form_valid(form)
        return redirect('list_items')

class DetailItem(LoginRequiredMixin, generic.DetailView):
    model = Item
    template_name = 'inventory/detail_item.html'

class DetailList(LoginRequiredMixin, generic.ListView):
    model = Item
    template_name = 'inventory/list_items.html'


class UpdateItem(LoginRequiredMixin, generic.UpdateView):
    model = Item
    template_name = 'clients/update_client.html'
    fields = [  'name',
                'desc',
                'price',
                'cost',
                'quantity'
     ]
    success_url = reverse_lazy('list_items')

    def get_object(self):
        item = super(UpdateItem, self).get_object()
        if not item.user == self.request.user:
            raise Http404
        return item

class DeleteItem(LoginRequiredMixin, generic.DeleteView):
    model = Item
    template_name = 'inventory/delete_item.html'
    success_url = reverse_lazy('list_items')

    def get_object(self):
        item = super(DeleteItem, self).get_object()
        if not client.user == self.request.user:
            raise Http404
        return item
