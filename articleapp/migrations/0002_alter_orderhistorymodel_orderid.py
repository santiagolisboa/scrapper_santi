# Generated by Django 3.2.8 on 2021-10-23 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistorymodel',
            name='orderId',
            field=models.CharField(help_text='order id', max_length=200),
        ),
    ]
