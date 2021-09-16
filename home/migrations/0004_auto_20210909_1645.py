# Generated by Django 3.2.5 on 2021-09-09 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_category_image_image_category_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='author',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='author',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='product',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]