from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import CustomerLedger
from .forms import CustomerLedgerForm
from customer.models import Customer


class CustomerLedgerListView(ListView):
    model = CustomerLedger
    template_name = 'customer/customer_ledger_list.html'
    paginate_by = 100

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            CustomerLedgerListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self, **kwargs):

        queryset = self.queryset

        if not queryset:
            queryset = self.model.objects.filter(
                customer__id=self.kwargs.get('pk')).order_by('-date')

        if self.request.GET.get('date'):
            queryset = queryset.filter(
                date__icontains=self.request.GET.get('date')
            )

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(
            CustomerLedgerListView, self).get_context_data(**kwargs)

        try:
            customer = Customer.objects.get(id=self.kwargs.get('pk'))
        except Customer.DoesNotExist:
            raise Http404('Customer does not exits!')

        context.update({
            'customer': customer
        })
        return context


class DebitCustomerLedgerFormView(FormView):
    template_name = 'customer/debit.html'
    form_class = CustomerLedgerForm

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            DebitCustomerLedgerFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(
            reverse('customer_ledger:ledger_list',
                    kwargs={'pk': obj.customer.id}
                    )
        )

    def get_context_data(self, **kwargs):
        context = super(
            DebitCustomerLedgerFormView, self).get_context_data(**kwargs)
        try:
            customer = Customer.objects.get(id=self.kwargs.get('pk'))
        except Customer.DoesNotExist:
            raise Http404('Customer does not exits!')

        context.update({
            'customer': customer
        })
        return context


class CreditCustomerLedgerFormView(DebitCustomerLedgerFormView):
    template_name = 'customer/credit.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            CreditCustomerLedgerFormView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(
            CreditCustomerLedgerFormView, self).get_context_data(**kwargs)
        try:
            customer = Customer.objects.get(id=self.kwargs.get('pk'))
        except Customer.DoesNotExist:
            raise Http404('Customer does not exits!')

        context.update({
            'customer': customer
        })
        return context