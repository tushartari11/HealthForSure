# Generated by Django 5.0.2 on 2024-04-24 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_medicines'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Medicines',
            new_name='Medicine',
        ),
    ]
