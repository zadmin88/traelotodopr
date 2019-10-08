from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
        #clients
        path('create', views.CreateClient.as_view(), name='create_client'),
        path('<int:pk>', views.detail_client, name='detail_client'),
        path('<int:pk>/update', views.UpdateClient.as_view(), name='update_client'),
        path('<int:pk>/delete', views.DeleteClient.as_view(), name='delete_client'),
        path('list', views.DetailList.as_view(), name='list_clients'),

]
