# Generated by Django 4.2 on 2023-04-15 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]