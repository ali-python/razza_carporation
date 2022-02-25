from django.db import models
from django.db.models import Sum
from django.utils import timezone

class Customer(models.Model):
	TYPE_CUSTOMER = 'customer'
	TYPE_SUPPLIER = 'supplier'

	TYPE_CS = (
		(TYPE_CUSTOMER, 'customer'),
		(TYPE_SUPPLIER, 'supplier')
		)
	type_cs = models.CharField(max_length=100, choices=TYPE_CS, default=TYPE_CUSTOMER)
	name = models.CharField(max_length=200)
	father_name = models.CharField(max_length=200, null=True, blank=True)
	cnic = models.CharField(max_length=200)
	mobile = models.CharField(max_length=200, null=True, blank=True)
	alternate_mobile = models.CharField(max_length=200, null=True, blank=True)
	resident = models.CharField(max_length=200, null=True, blank=True)
	address = models.CharField(max_length=200, null=True, blank=True)
	city = models.CharField(max_length=200, null=True, blank=True)
	ntn = models.CharField(max_length=200, null=True, blank=True)
	strn = models.CharField(max_length=200, null=True, blank=True)
	date = models.DateField(default=timezone.now, null=True, blank=True)

	def __str__(self):
		return self.name

	def get_unpaid_amount(self):
		customer_ledgers = self.customer_ledger.all()

		if customer_ledgers:
			ledger_debit = customer_ledgers.aggregate(Sum('debit_amount'))
			ledger_credit = customer_ledgers.aggregate(Sum('credit_amount'))

			debit_amount = ledger_debit.get('debit_amount__sum')
			credit_amount = ledger_credit.get('credit_amount__sum')
		else:
			debit_amount = 0
			credit_amount = 0

		unpaid_amount = debit_amount - credit_amount
		return unpaid_amount