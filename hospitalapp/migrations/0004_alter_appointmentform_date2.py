# Generated by Django 5.0.6 on 2024-06-25 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_alter_healthcaresolutions_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentform',
            name='date2',
            field=models.TimeField(),
        ),
    ]
