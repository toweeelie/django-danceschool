# Generated by Django 3.1.6 on 2021-02-20 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_invoiceitem_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='taxRate',
            field=models.FloatField(help_text='This rate is used to update the tax line item when discounts or other pre-tax price adjustments are applied.  Enter as a whole number (e.g. 6 for 6%).', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Sales tax rate'),
        ),
    ]
