# Generated by Django 3.0.7 on 2020-07-24 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msat', '0004_msat_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msat',
            name='email',
        ),
        migrations.RemoveField(
            model_name='msat',
            name='r_id',
        ),
        migrations.RemoveField(
            model_name='msat',
            name='stud_id',
        ),
    ]
