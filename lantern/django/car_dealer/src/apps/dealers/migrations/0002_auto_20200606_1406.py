# Generated by Django 3.0.7 on 2020-06-06 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='dealer',
            name='dealers_dea_title_d94ffd_idx',
        ),
        migrations.RemoveField(
            model_name='dealer',
            name='title',
        ),
    ]
