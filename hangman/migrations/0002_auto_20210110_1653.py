# Generated by Django 3.1.5 on 2021-01-10 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Phrases',
            new_name='Phrase',
        ),
    ]
