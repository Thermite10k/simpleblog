# Generated by Django 3.2.6 on 2021-08-27 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0011_post_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
