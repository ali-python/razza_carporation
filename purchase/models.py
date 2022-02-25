from django.db import models
from django.utils import timezone
from django.db.models import Sum
from product.models import ProductCategory
from customer.models import Customer
from vehicle.models import Vehicle

class Purchase(models.Model):
	item = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,
							 null=True, blank=True, related_name='purchase_item')
	supplier = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True,
								related_name= 'purchase_supplier')
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True,
								related_name= 'purchase_vehicle')
	price_per_ton = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True)
	advance_payment = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True)
	after_advance_payment = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True)
	expense_per_ton = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True)
	total_ton = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True)
	frieght = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True)
	cost = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True)
	total_cost = models.DecimalField(max_digits=65, decimal_places=2, default=0, null=True, blank=True)
	bilty = models.CharField(max_length=100, null=True, blank=True)
	bilty_image = models.ImageField(upload_to="bilty/img/", null=True, blank=True)
	date = models.DateField(default=timezone.now, null=True, blank=True)

	def __str__(self):
		return self.item
