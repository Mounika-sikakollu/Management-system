# Generated by Django 4.2 on 2023-10-12 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_datef_feedback_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='author',
        ),
    ]
