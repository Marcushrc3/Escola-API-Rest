# Generated by Django 4.0.5 on 2022-06-05 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='codigo_curdo',
            new_name='codigo_curso',
        ),
    ]
