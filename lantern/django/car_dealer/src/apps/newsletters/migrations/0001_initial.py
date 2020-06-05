# Generated by Django 3.0.7 on 2020-06-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name': 'NewsLetter',
                'verbose_name_plural': 'NewsLetters',
                'ordering': ['email'],
            },
        ),
    ]
