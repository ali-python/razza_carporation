from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import Purchase
from .forms import PurchaseForm
from customer.models import Customer
from product.models import ProductCategory
from vehicle.models import	Vehicle


class AddPurchase(FormView):
    form_class = PurchaseForm
    template_name = 'purchase/create_purchase.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            AddPurchase, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('purchase:list'))

    def form_invalid(self, form):
        return super(AddPurchase, self).form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super(AddPurchase, self).get_context_data(**kwargs)
        context.update({
            'item': ProductCategory.objects.all(),
            'supplier': Customer.objects.filter(type_cs='supplier'),
            'vehicle': Vehicle.objects.all()
        })
        return context


class PurchaseList(ListView):
    model = Purchase
    template_name = 'purchase/list_purchase.html'
    paginate_by = 100
    ordering = 'id'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            PurchaseList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        if not queryset:
            queryset = Purchase.objects.all().order_by('id')

        if self.request.GET.get('purchase_id'):
            queryset = queryset.filter(
                cnic=self.request.GET.get('purchase_id').lstrip('0')
            )

        return queryset.order_by('id')


class PurchaseDetailTemplateView(TemplateView):
    template_name = 'purchase/detail_purchase.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            PurchaseDetailTemplateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PurchaseDetailTemplateView, self).get_context_data(**kwargs)
        context.update({
            'purchase': Purchase.objects.get(id=self.kwargs.get('pk')),
        })
        return context