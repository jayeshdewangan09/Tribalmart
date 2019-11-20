# Generated by Django 2.2.4 on 2019-10-13 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20191004_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='itemsJson',
            new_name='items_json',
        ),
        migrations.AlterField(
            model_name='customerquery',
            name='query_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 13, 22, 22, 30, 100346), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 13, 22, 22, 30, 100346), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='update_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 13, 22, 22, 30, 101350), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 13, 22, 22, 30, 98352), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.CharField(default=datetime.datetime(2019, 10, 13, 22, 22, 30, 99349), max_length=50),
        ),
        migrations.AlterField(
            model_name='product_request',
            name='pub_date',
            field=models.CharField(default=datetime.datetime(2019, 10, 13, 22, 22, 30, 99349), max_length=50),
        ),
        migrations.AlterField(
            model_name='product_request',
            name='request_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 13, 22, 22, 30, 99349), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pulled_requests',
            name='product_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 13, 22, 22, 30, 99349), max_length=50, primary_key=True, serialize=False),
        ),
    ]
