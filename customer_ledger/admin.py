from django.contrib import admin
from .models import CustomerLedger


class CustomerLegerAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'debit_amount', 'credit_amount', 'invoice', 'details', 'date'
    )

    @staticmethod
    def invoice(obj):
        return str(obj.invoice.id).zfill(7) if obj.invoice else ''

admin.site.register(CustomerLedger, CustomerLegerAdmin)
