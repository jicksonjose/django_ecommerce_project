# Generated by Django 4.2 on 2023-05-08 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_orders_pin_orders_state_alter_orders_address_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='payment_details',
        ),
        migrations.DeleteModel(
            name='userlogin',
        ),
        migrations.AddField(
            model_name='orders',
            name='cancel_request',
            field=models.CharField(default='none', max_length=100),
        ),
    ]