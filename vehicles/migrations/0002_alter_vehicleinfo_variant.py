# Generated by Django 5.0.3 on 2024-04-04 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleinfo',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.variantinfo', verbose_name='车型'),
        ),
    ]