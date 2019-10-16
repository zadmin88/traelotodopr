from django.shortcuts               import render
from django.shortcuts               import render, redirect
from django.urls                    import reverse_lazy
from django.views                   import generic
from django.contrib.auth.forms      import UserCreationForm
from django.contrib.auth            import authenticate, login
# from .forms import VideoForm, SearchForm
from django.forms                   import formset_factory
from django.http                    import Http404, JsonResponse
from django.forms.utils             import ErrorList
import urllib
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins     import LoginRequiredMixin
from clients.models                 import Client
from inventory.models               import Item
from invoices.models                import Invoice

def home(request):
    if request.user.is_authenticated:
        item    = Item.objects.filter(user = request.user).order_by('-id')[:5][::-1]
        client  = Client.objects.filter(user = request.user).order_by('-id')[:5][::-1]
        invoice = Invoice.objects.filter(user = request.user).order_by('-id')[:5][::-1]
        return render(request, 'accounts/home.html', {'item':item,'client':client,'invoice':invoice})
    else:
        return render(request, 'accounts/home.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view
