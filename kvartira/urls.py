from django.urls import path
from .views import *

urlpatterns = [
    path('', Kvartira_list.as_view(), name='kvartira'),
    path('kvartera/<int:pk>/', Kvartira_detal.as_view(), name='kvartera_detal'),
    path('create/', Kvartira_create.as_view(), name='kvartira_create'),
    path('kvartera/update/<int:pk>/', Kvartera_update.as_view(), name='kvartera_update'),
    path('kvartera/delete/<int:pk>/', Kvartera_delete.as_view(), name='kvartera_delete'),

]
