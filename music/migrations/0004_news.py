# Generated by Django 4.0.6 on 2022-07-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_delete_music2'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_name', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
    ]