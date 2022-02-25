from django.contrib import admin
from .models import Sales


class SalesAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'customer', 'item', 'vehicle', 'price_per_ton','total_ton', 'total_amount', 'deduction',
        'frieght_recieved', 'sub_total', 'balance', 'date'
    )


admin.site.register(Sales, SalesAdmin)

