from django.urls import path

from .views import add_customer

app_name = 'customers'

urlpatterns = [
    path('add_customer/', add_customer, name='add_customer'),
]
