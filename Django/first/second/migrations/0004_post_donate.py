# Generated by Django 4.1.7 on 2023-04-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0003_category_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='donate',
            field=models.FloatField(default=0),
        ),
    ]