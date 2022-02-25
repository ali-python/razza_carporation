from django import forms
from .models import CustomerLedger


class CustomerLedgerForm(forms.ModelForm):
    class Meta:
        model = CustomerLedger
        fields = '__all__'