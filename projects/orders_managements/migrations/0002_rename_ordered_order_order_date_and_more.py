# Generated by Django 4.2.6 on 2023-10-26 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders_managements', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Ordered',
            new_name='order_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='OrderId',
            new_name='order_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Order_status',
            new_name='order_orderstatus',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Shipped',
            new_name='order_shipped',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ShippingAdress',
            new_name='order_shippingadresse',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Total',
            new_name='order_total',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='UserName',
            new_name='order_username',
        ),
    ]
