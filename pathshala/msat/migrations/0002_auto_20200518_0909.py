# Generated by Django 3.0.6 on 2020-05-18 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msat',
            name='answered',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='msat',
            name='response',
            field=models.CharField(max_length=500),
        ),
    ]
