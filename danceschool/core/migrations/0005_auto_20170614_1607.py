# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-14 16:07
from __future__ import unicode_literals

import danceschool.core.mixins
import danceschool.core.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20170517_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('validationString', models.CharField(default=danceschool.core.models.get_validationString, editable=False, max_length=25, verbose_name='Validation string')),
                ('creationDate', models.DateTimeField(auto_now_add=True, verbose_name='Invoice created')),
                ('modifiedDate', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('status', models.CharField(choices=[('U', 'Unpaid'), ('A', 'Authorized using payment processor'), ('P', 'Paid'), ('N', 'Cash payment recorded'), ('R', 'Refunded in full'), ('C', 'Cancelled'), ('X', 'Rejected in processing'), ('E', 'Error in processing')], default='U', max_length=1, verbose_name='Payment status')),
                ('paidOnline', models.BooleanField(default=False, verbose_name='Paid Online')),
                ('grossTotal', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total before discounts')),
                ('total', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total billed amount')),
                ('adjustments', models.FloatField(default=0, verbose_name='Refunds/adjustments')),
                ('taxes', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Taxes')),
                ('fees', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Processing fees')),
                ('amountPaid', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Net Amount Paid')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comments')),
                ('data', models.JSONField(default=dict)),
                ('collectedByUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collectedinvoices', to=settings.AUTH_USER_MODEL, verbose_name='Collected by user')),
            ],
            options={
                'permissions': (('view_all_invoices', 'Can view invoices without passing the validation string.'), ('send_invoices', 'Can send invoices to students requesting payment'), ('process_refunds', 'Can refund customers for registrations and other invoice payments.')),
            },
            bases=(danceschool.core.mixins.EmailRecipientMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('grossTotal', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total before discounts')),
                ('total', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total billed amount')),
                ('adjustments', models.FloatField(default=0, verbose_name='Refunds/adjustments')),
                ('taxes', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Taxes')),
                ('fees', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Processing fees')),
            ],
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ('-dateTime',), 'permissions': (('view_registration_summary', 'Can access the series-level registration summary view'), ('checkin_customers', 'Can check-in customers using the summary view'), ('accept_door_payments', 'Can process door payments in the registration system'), ('register_dropins', 'Can register students for drop-ins.'), ('override_register_closed', 'Can register students for series/events that are closed for registration by the public'), ('override_register_soldout', 'Can register students for series/events that are officially sold out'), ('override_register_dropins', 'Can register students for drop-ins even if the series does not allow drop-in registration.'))},
        ),
        migrations.RemoveField(
            model_name='registration',
            name='amountPaid',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='collectedByUser',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='invoiceNumber',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='paidOnline',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='processingFee',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='submissionUser',
        ),
        migrations.AlterUniqueTogether(
            name='eventregistration',
            unique_together=set([('registration', 'event')]),
        ),
        migrations.AlterUniqueTogether(
            name='temporaryeventregistration',
            unique_together=set([('registration', 'event')]),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='finalEventRegistration',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.EventRegistration', verbose_name='Event registration'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Invoice', verbose_name='Invoice'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='temporaryEventRegistration',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.TemporaryEventRegistration', verbose_name='Temporary event registration'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='finalRegistration',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Registration', verbose_name='Registration'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='submissionUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submittedinvoices', to=settings.AUTH_USER_MODEL, verbose_name='registered by user'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='temporaryRegistration',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.TemporaryRegistration', verbose_name='Temporary registration'),
        ),
    ]
