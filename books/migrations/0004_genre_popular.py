# Generated by Django 2.0.7 on 2018-07-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='popular',
            field=models.BooleanField(default=False),
        ),
    ]