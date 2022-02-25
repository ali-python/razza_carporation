from django.db import models
from django.db.models import Sum
from django.utils import timezone
from sales.models import Sales
from customer.models import Customer



class CustomerLedger(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='customer_ledger'
    )
    invoice = models.ForeignKey(
        Sales, related_name='invoice_ledger', blank=True, null=True, on_delete=models.CASCADE
    )
    debit_amount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )
    credit_amount = models.DecimalField(
        max_digits=65, decimal_places=2, default=0, blank=True, null=True
    )
    details = models.TextField(max_length=500, blank=True, null=True)
    date = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.customer.name
