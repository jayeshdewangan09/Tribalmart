# Generated by Django 2.2.4 on 2019-10-02 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20191002_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerquery',
            name='query_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 14, 6, 28, 911672), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 14, 6, 28, 911672), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 14, 6, 28, 909678), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 14, 6, 28, 909678), max_length=50),
        ),
        migrations.AlterField(
            model_name='product_request',
            name='pub_date',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 14, 6, 28, 910675), max_length=50),
        ),
        migrations.AlterField(
            model_name='product_request',
            name='request_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 14, 6, 28, 910675), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pulled_requests',
            name='product_id',
            field=models.CharField(default=datetime.datetime(2019, 10, 2, 14, 6, 28, 910675), max_length=50, primary_key=True, serialize=False),
        ),
    ]
