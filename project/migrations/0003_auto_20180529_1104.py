# Generated by Django 2.0.5 on 2018-05-29 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20180529_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_modules',
            name='end_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project_modules',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.Employee'),
        ),
    ]