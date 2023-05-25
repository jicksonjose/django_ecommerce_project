# Generated by Django 4.1.5 on 2023-02-20 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_item_review_alter_cartproduct_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category_id',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whislist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user_details'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wishlist_products',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.item'),
        ),
    ]
