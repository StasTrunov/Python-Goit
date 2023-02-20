# Generated by Django 4.1.7 on 2023-02-20 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_remove_programer_languages_processing_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tennis_players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.FloatField()),
                ('height', models.FloatField()),
                ('ranked_in_ATP', models.FloatField()),
                ('majors', models.PositiveIntegerField(default=0)),
                ('like', models.PositiveIntegerField(default=0)),
                ('dislike', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Programer_languages',
            new_name='Prog_languages',
        ),
        migrations.DeleteModel(
            name='Tennis_payers',
        ),
    ]
