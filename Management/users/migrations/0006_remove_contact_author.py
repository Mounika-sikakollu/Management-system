# Generated by Django 4.2 on 2023-10-12 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_feedback_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='author',
        ),
    ]
