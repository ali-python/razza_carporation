from django.db import models
from django.utils import timezone
from django.db.models import Sum
from purchase.models import Purchase
from customer.models import Customer
from product.models import ProductCategory
from vehicle.models import Vehicle

class Sales(models.Model):
	item = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,
							 null=True, blank=True, related_name='sales_item')
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE,
							 null=True, blank=True, related_name='sales_vehicle')
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
							 null=True, blank=True, related_name='sales_customer')
	price_per_ton = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True) 
	total_ton = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True) 
	total_amount = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True) 
	deduction = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True) 
	frieght_recieved = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True) 
	sub_total = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True) 
	balance = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True) 
	advance_payment = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True) 
	gst = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True) 
	gst_sub_total = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True) 
	paid_amount = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True) 
	remaining_payment = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True) 
	date = models.DateField(default=timezone.now, null=True, blank=True)

	def __str__(self):
		return self.customer.name