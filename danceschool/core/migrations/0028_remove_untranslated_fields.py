# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-14 22:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_migrate_translatable_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staffmember',
            options={'ordering': ('translations__lastName', 'translations__firstName'), 'permissions': (('view_staff_directory', 'Can access the staff directory view'), ('view_school_stats', "Can view statistics about the school's performance."), ('can_autocomplete_staffmembers', 'Able to use customer and staff member autocomplete features (in admin forms)')), 'verbose_name': 'Staff member', 'verbose_name_plural': 'Staff members'},
        ),
        migrations.AlterUniqueTogether(
            name='staffmember',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='staffmembertranslation',
            unique_together=set([('language_code', 'master'), ('language_code', 'firstName', 'lastName')]),
        ),
        migrations.RemoveField(
            model_name='staffmember',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='staffmember',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='staffmember',
            name='lastName',
        ),
    ]
