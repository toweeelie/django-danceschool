# Generated by Django 3.1.13 on 2023-09-27 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0053_merge_20210325_1619'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Competition name')),
                ('stage', models.CharField(choices=[('r', 'Registration'), ('p', 'Prelims'), ('d', 'Draw'), ('f', 'Finals')], default='r', max_length=12)),
                ('finalists_number', models.IntegerField(verbose_name='Number of finalists per dance role')),
                ('pair_finalists', models.BooleanField(blank=True, default=True, verbose_name='Paired Final')),
                ('results_visible', models.BooleanField(default=False, verbose_name='Publish results')),
                ('comp_roles', models.ManyToManyField(to='core.DanceRole', verbose_name='Dance roles')),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prelims', models.BooleanField(default=False, verbose_name='Judging Prelims')),
                ('prelims_main_judge', models.BooleanField(default=False, verbose_name='Prelims Main Judge')),
                ('finals', models.BooleanField(default=False, verbose_name='Judging Finals')),
                ('finals_main_judge', models.BooleanField(default=False, verbose_name='Finals Main Judge')),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.competition')),
                ('prelims_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dancerole')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('profile', 'comp')},
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_num', models.IntegerField()),
                ('comp_checked_in', models.BooleanField(default=False, verbose_name='Checked In')),
                ('finalist', models.BooleanField(default=False, verbose_name='Finalist')),
                ('final_heat_order', models.IntegerField(default=0)),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.competition')),
                ('comp_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dancerole', verbose_name='Dance Role')),
                ('competitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer', verbose_name='Competitor')),
                ('final_partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competitions.registration', verbose_name='Partner in final')),
            ],
            options={
                'unique_together': {('comp', 'competitor')},
            },
        ),
        migrations.CreateModel(
            name='PrelimsResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=100)),
                ('result', models.CharField(choices=[('yes', 'Y'), ('maybe', 'Mb'), ('no', '')], default='no', max_length=10)),
                ('comp_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.registration')),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.judge')),
            ],
            options={
                'unique_together': {('judge', 'comp_reg')},
            },
        ),
        migrations.CreateModel(
            name='FinalsResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=100)),
                ('result', models.IntegerField(verbose_name='Place')),
                ('comp_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.registration')),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.judge')),
            ],
            options={
                'unique_together': {('judge', 'comp_reg')},
            },
        ),
    ]
