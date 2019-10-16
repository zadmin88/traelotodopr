from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
        #items
        path('create', views.CreateItem.as_view(), name='create_item'),
        path('<int:pk>', views.DetailItem.as_view(), name='detail_item'),
        path('<int:pk>/update', views.UpdateItem.as_view(), name='update_item'),
        path('<int:pk>/delete', views.DeleteItem.as_view(), name='delete_item'),
        path('list', views.detail_list, name='list_items'),

]
