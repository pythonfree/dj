# Generated by Django 3.0.4 on 2020-03-08 07:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artilce',
            new_name='Article',
        ),
    ]