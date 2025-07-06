from django.urls import path
from .views import home, aloqa

urlpatterns = [
    path('', home, name='home'),
    path('aloqa/', aloqa, name='aloqa'),
]