from django.urls import path
from .views import (
    CustomerLedgerListView, DebitCustomerLedgerFormView,CreditCustomerLedgerFormView
)

urlpatterns = [
	path(
        '<int:pk>/ledger/list/',
        CustomerLedgerListView.as_view(),
        name='ledger_list'
    ),
    path(
        '<int:pk>/ledger/debit/',
        DebitCustomerLedgerFormView.as_view(),
        name='ledger_debit'
    ),
    path(
        '<int:pk>/ledger/credit/',
        CreditCustomerLedgerFormView.as_view(),
        name='ledger_credit'
    )
		
    ]