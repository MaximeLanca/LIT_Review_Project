# Generated by Django 5.1.5 on 2025-06-12 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_alter_review_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ticket',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='activity.ticket'),
        ),
    ]
