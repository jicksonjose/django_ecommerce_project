# Generated by Django 4.2.1 on 2023-05-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_alter_orders_order_status_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_address',
            name='email',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
