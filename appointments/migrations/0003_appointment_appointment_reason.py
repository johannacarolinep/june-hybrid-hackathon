# Generated by Django 4.2.13 on 2024-06-13 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_reason',
            field=models.CharField(default='', max_length=50),
        ),
    ]