# Generated by Django 5.0.2 on 2024-04-24 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_medicines_medicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='image',
            field=models.ImageField(default='', upload_to='home/images'),
        ),
    ]