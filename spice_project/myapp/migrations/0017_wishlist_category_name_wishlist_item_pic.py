# Generated by Django 4.2 on 2023-04-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_wishlist_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='category_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='item_pic',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
