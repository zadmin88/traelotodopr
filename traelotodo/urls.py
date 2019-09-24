
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path, include
from accounts import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # AUTH
    path('accounts/', include('accounts.urls')),
    path('clients/', include('clients.urls')),
    path('inventory/', include('inventory.urls')),
    path('invoice/', include('invoices.urls')),
]
