# Generated by Django 2.2.12 on 2020-06-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200614_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastercontrol',
            name='event_name',
            field=models.CharField(default='MississaugaHacks2020', max_length=20),
        ),
    ]
