# Generated by Django 2.0.13 on 2019-03-09 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pdf',
            new_name='file',
        ),
    ]
