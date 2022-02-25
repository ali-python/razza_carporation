from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, FormView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import Sales
from .forms import SalesForm
from customer.models import Customer
from customer_ledger.forms import CustomerLedgerForm
from product.models import ProductCategory
from vehicle.models import	Vehicle


class AddSales(FormView):
    form_class = SalesForm
    template_name = 'sales/create_sales.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            AddSales, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        sales_invoice = form.save()
        remaining_payment = self.request.POST.get('remaining_payment')
        if float(remaining_payment):
            ledger_form_kwargs = {
                'customer' : sales_invoice.customer.id,
                'invoice' : sales_invoice.id,
                'debit_amount' : remaining_payment,
                'details' : ('Remaining Payment for Bill/Receipt No %s'
                    % str(sales_invoice.id).zfill(7)),
                'date' : timezone.now()

            }
            customer_ledger = CustomerLedgerForm(ledger_form_kwargs)
            customer_ledger.save()
        return HttpResponseRedirect(reverse('sales:list'))

    def form_invalid(self, form):
        return super(AddSales, self).form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super(AddSales, self).get_context_data(**kwargs)
        context.update({
            'item': ProductCategory.objects.all(),
            'customer': Customer.objects.filter(type_cs='customer'),
            'vehicle': Vehicle.objects.all()
        })
        return context


class SalesList(ListView):
    model = Sales
    template_name = 'sales/list_sales.html'
    paginate_by = 100
    ordering = 'id'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            SalesList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        if not queryset:
            queryset = Sales.objects.all().order_by('id')

        if self.request.GET.get('sales_id'):
            queryset = queryset.filter(
                cnic=self.request.GET.get('sales_id').lstrip('0')
            )

        return queryset.order_by('id')


class SalesDetailTemplateView(TemplateView):
    template_name = 'sales/detail_sales.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            SalesDetailTemplateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SalesDetailTemplateView, self).get_context_data(**kwargs)
        context.update({
            'sales': Sales.objects.get(id=self.kwargs.get('pk')),
        })
        return context