# Generated by Django 4.1.7 on 2023-02-20 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_product_dislike_product_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programer_languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('processing', models.Field()),
                ('speed', models.Field()),
                ('date_of_creation', models.DateField(blank=True, null=True)),
                ('like', models.PositiveIntegerField(default=0)),
                ('dislike', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tennis_payers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.FloatField()),
                ('height', models.FloatField()),
                ('ranked_in_ATP', models.FloatField()),
                ('majors', models.FloatField()),
                ('like', models.PositiveIntegerField(default=0)),
                ('dislike', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
