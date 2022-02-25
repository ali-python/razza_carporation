from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from customer.models import Customer
from customer.forms import CustomerForm
from sales.models import Sales


class AddCustomer(FormView):
    form_class = CustomerForm
    template_name = 'customer/create_customer.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            AddCustomer, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('customer:list'))

    def form_invalid(self, form):
        return super(AddCustomer, self).form_invalid(form)


class CustomerList(ListView):
    model = Customer
    template_name = 'customer/list_customer.html'
    paginate_by = 100
    ordering = 'name'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            CustomerList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        if not queryset:
            queryset = Customer.objects.all().order_by('name')

        if self.request.GET.get('customer_name'):
            queryset = queryset.filter(
                name__icontains=self.request.GET.get('customer_name'))

        if self.request.GET.get('customer_id'):
            queryset = queryset.filter(
                cnic=self.request.GET.get('customer_id').lstrip('0')
            )

        return queryset.order_by('name')


class CustomerInvoices(TemplateView):
    template_name = 'customer/customer_invoice_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return super(
            CustomerInvoices, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(
            CustomerInvoices, self).get_context_data(**kwargs)

        sales=Sales.objects.filter(
            customer__id=self.kwargs.get('pk'))
        customer = Customer.objects.get(id=self.kwargs.get('pk'))
        
        context.update({
            'sales':sales,
            'customer':customer
        })

        return context


class DeleteCustomer(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer:list')
    success_message = ''

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            DeleteProduct, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)