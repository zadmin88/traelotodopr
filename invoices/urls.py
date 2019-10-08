from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
        #items
        path('create', views.create_invoice, name='create_invoice'),
        path('update_total', views.update_total, name='update_total'),
        path('list', views.InvoicesList.as_view(), name='list_invoices'),
        # path('<int:pk>', views.DetailInvoice.as_view(), name='detail_invoice'),
        path('<int:pk>', views.detail_invoice, name='detail_invoice'),
        path('<int:pk>/delete', views.DeleteInvoice.as_view(), name='delete_invoice'),
        # path('<int:pk>', views.DetailItem.as_view(), name='detail_item'),
        # path('<int:pk>/update', views.UpdateItem.as_view(), name='update_item'),
        # path('<int:pk>/delete', views.DeleteItem.as_view(), name='delete_item'),
        # path('list', views.DetailList.as_view(), name='list_items'),

]
