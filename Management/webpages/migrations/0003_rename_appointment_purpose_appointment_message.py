# Generated by Django 4.2 on 2023-10-18 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_rename_appointment_purpose_appointment_appointment_purpose'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='appointment_purpose',
            new_name='message',
        ),
    ]
