# Generated by Django 4.2 on 2023-04-30 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_wishlist_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.user_details'),
            preserve_default=False,
        ),
    ]