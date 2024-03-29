# Generated by Django 4.1.7 on 2023-03-07 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
                ('height', models.FloatField()),
                ('costs', models.FloatField()),
                ('club', models.ManyToManyField(to='homework1.fclub')),
            ],
        ),
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=60)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework1.fclub')),
            ],
        ),
    ]
