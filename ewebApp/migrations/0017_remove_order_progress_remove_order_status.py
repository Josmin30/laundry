# Generated by Django 5.0.3 on 2024-04-04 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ewebApp', '0016_delete_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='progress',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]