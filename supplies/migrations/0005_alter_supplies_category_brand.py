# Generated by Django 5.0.3 on 2024-04-04 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0004_alter_suppliesinfo_price'),
        ('vehicles', '0002_alter_vehicleinfo_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplies_category',
            name='brand',
            field=models.ForeignKey(default='通用', on_delete=django.db.models.deletion.CASCADE, to='vehicles.brandinfo', verbose_name='适用品牌'),
        ),
    ]