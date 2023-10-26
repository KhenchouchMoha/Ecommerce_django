# Generated by Django 4.2.6 on 2023-10-26 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_managements', '0003_alter_products_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='categories',
            new_name='product_categories',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='descriptions',
            new_name='product_descriptions',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='discount',
            new_name='product_discount',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='in_stock',
            new_name='product_in_stock',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='price',
            new_name='product_price',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='quantite',
            new_name='product_quantite',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='title',
            new_name='product_title',
        ),
    ]
