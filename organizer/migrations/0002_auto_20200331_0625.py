# Generated by Django 3.0.4 on 2020-03-31 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(related_name='startups', to='organizer.Tag'),
        ),
    ]