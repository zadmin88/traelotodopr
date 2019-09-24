from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
        # clients
        # path('inventario/create', views.CreateInvent.as_view(), name='create_invent'),
        # path('clients/<int:pk>', views.DetailHall.as_view(), name='detail_client'),
        # path('clients/<int:pk>/update', views.UpdateHall.as_view(), name='update_client'),
        # path('clients/<int:pk>/delete', views.DeleteHall.as_view(), name='delete_client'),

]
