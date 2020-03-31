# Generated by Django 3.0.4 on 2020-03-31 06:38

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_auto_20200331_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslink',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=31, populate_from=['title']),
        ),
        migrations.AlterField(
            model_name='startup',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='A label for URL config.', max_length=31, populate_from=['name']),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='A label for URL config.', max_length=31, populate_from=['name']),
        ),
    ]
