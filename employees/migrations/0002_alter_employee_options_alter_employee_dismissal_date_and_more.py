# Generated by Django 4.2.4 on 2023-08-29 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='dismissal_date',
            field=models.DateField(blank=True, null=True, verbose_name='dismissal_date'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employment_date',
            field=models.DateField(verbose_name='employment_date'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_employee_active'),
        ),
    ]