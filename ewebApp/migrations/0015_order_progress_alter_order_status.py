# Generated by Django 5.0.3 on 2024-04-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewebApp', '0014_delete_item_delete_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='progress',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
