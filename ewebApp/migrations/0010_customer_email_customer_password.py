# Generated by Django 5.0.3 on 2024-04-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewebApp', '0009_remove_order_manager_order_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
