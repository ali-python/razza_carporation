# Generated by Django 3.2.12 on 2022-02-13 09:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0003_auto_20220212_1557'),
        ('customer', '0003_auto_20220212_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerLedger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('credit_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('details', models.TextField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_ledger', to='customer.customer')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_ledger', to='sales.sales')),
            ],
        ),
    ]
