# Generated by Django 5.1.5 on 2025-02-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.FileField(upload_to='tickets/'),
        ),
    ]
