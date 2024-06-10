# Generated by Django 4.2 on 2024-06-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaming', '0002_country_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='prefix',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='player',
            name='draws',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='games_played',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='losses',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='wins',
            field=models.PositiveIntegerField(default=0),
        ),
    ]