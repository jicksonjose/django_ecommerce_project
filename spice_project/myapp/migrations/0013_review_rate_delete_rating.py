# Generated by Django 4.2 on 2023-04-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_rating_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='rating',
        ),
    ]
