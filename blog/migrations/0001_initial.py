# Generated by Django 3.0.4 on 2020-03-31 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(max_length=63)),
                ('text', models.TextField()),
                ('pub_date', models.DateField(verbose_name='Date Published')),
                ('startups', models.ManyToManyField(to='organizer.Startup')),
                ('tags', models.ManyToManyField(to='organizer.Tag')),
            ],
            options={
                'verbose_name': 'Blog Post',
                'ordering': ['-pub_date', 'title'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]
