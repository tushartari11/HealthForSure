# Generated by Django 5.0.2 on 2024-03-31 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_patient_addnewpatient'),
    ]

    operations = [
        migrations.AddField(
            model_name='addnewpatient',
            name='medicines',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='addnewpatient',
            name='fullname',
            field=models.CharField(max_length=50),
        ),
    ]
