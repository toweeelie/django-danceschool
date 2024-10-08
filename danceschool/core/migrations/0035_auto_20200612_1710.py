# Generated by Django 2.2.13 on 2020-06-12 14:10

from django.db import migrations, models
import django.db.models.deletion
import parler.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_merge_20200516_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='sheet_id',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Sheet ID'),
        ),
        migrations.AlterField(
            model_name='staffmembertranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='core.StaffMember'),
        ),
    ]
