# Generated by Django 5.0.3 on 2024-04-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_records', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairrecord',
            name='RecordName',
            field=models.CharField(choices=[('维修', '维修'), ('保养', '保养')], max_length=2, verbose_name='维保种类'),
        ),
    ]
