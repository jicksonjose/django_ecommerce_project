# Generated by Django 4.2 on 2023-05-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_user_details_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_description',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='original_rate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
