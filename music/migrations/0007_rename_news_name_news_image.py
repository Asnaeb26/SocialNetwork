# Generated by Django 4.0.6 on 2022-07-20 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_news_news_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='news_name',
            new_name='image',
        ),
    ]
