# Generated by Django 4.2.3 on 2023-08-28 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_product_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user',
            new_name='owner',
        ),
    ]