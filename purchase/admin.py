from django.contrib import admin
from .models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'item', 'supplier', 'vehicle', 'price_per_ton', 'expense_per_ton',
        'total_ton', 'frieght', 'cost', 'total_cost', 'bilty', 'bilty_image', 'date'
    )


admin.site.register(Purchase, PurchaseAdmin)

