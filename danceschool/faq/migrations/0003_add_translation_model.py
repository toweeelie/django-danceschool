# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-13 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20170717_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('question', models.CharField(max_length=200, verbose_name='Question')),
                ('answer', djangocms_text_ckeditor.fields.HTMLField(help_text='Answer the question.', verbose_name='Answer')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='faq.FAQ')),
            ],
            options={
                'verbose_name': 'FAQ Translation',
                'managed': True,
                'db_table': 'faq_faq_translation',
                'default_permissions': (),
                'db_tablespace': '',
            },
        ),
        migrations.AlterUniqueTogether(
            name='faqtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
