# Generated by Django 3.2.6 on 2021-08-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_rename_category_category2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='...', max_length=255),
        ),
    ]
