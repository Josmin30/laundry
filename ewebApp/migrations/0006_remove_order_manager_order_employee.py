# Generated by Django 5.0.3 on 2024-04-01 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewebApp', '0005_order_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='manager',
        ),
        migrations.AddField(
            model_name='order',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ewebApp.employee'),
        ),
    ]
