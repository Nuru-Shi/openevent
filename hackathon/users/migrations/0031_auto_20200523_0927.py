# Generated by Django 2.2.12 on 2020-05-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='CHOICES',
            field=models.ManyToManyField(blank=True, null=True, to='users.Submission'),
        ),
    ]
