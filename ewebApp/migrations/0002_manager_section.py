# Generated by Django 5.0.3 on 2024-03-27 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewebApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='section',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
