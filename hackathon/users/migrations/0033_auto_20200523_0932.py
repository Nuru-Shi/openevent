# Generated by Django 2.2.12 on 2020-05-23 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_auto_20200523_0927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='SubmissionID',
            new_name='Score',
        ),
    ]