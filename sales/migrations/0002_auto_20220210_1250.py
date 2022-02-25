# Generated by Django 3.2.12 on 2022-02-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='gst',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='gst_sub_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True),
        ),
    ]
