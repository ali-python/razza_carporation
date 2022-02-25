from django.urls import path
from .views import (
    AddSales, SalesList, SalesDetailTemplateView
)

urlpatterns = [
    path('add/', AddSales.as_view(), name='add'),
    path('list/', SalesList.as_view(), name='list'),
    path('detail/<int:pk>/', SalesDetailTemplateView.as_view(), name='detail'),

]