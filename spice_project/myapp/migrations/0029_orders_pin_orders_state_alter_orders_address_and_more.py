# Generated by Django 4.2 on 2023-05-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_contact_support'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='pin',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='state',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='mobile',
            field=models.CharField(max_length=50),
        ),
    ]
