# Generated by Django 4.2.1 on 2023-05-25 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_order_address_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_address',
            name='email',
        ),
    ]