from django.urls import path
from customer.views import (
    AddCustomer, CustomerList,DeleteCustomer, CustomerInvoices
)

urlpatterns = [
    path('add/', AddCustomer.as_view(), name='add'),
    path('list/', CustomerList.as_view(), name='list'),
    path('delete//<int:pk>/', DeleteCustomer.as_view(), name='delete'),
    path('invoice/list/<int:pk>/', CustomerInvoices.as_view(), name='invoice_list'),
    ]