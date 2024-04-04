# Generated by Django 5.0.3 on 2024-04-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('repair_records', '0001_initial'),
        ('supplies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairrecord',
            name='usedSupplies',
            field=models.ManyToManyField(to='supplies.suppliesinfo', verbose_name='使用配件'),
        ),
    ]
