# Generated by Django 5.0.3 on 2024-04-02 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ewebApp', '0007_order_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='employee',
        ),
    ]
