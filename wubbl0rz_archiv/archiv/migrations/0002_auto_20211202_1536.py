# Generated by Django 3.2.9 on 2021-12-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vod',
            name='bitrate',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vod',
            name='format_note',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vod',
            name='fps',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vod',
            name='resolution',
            field=models.TextField(blank=True, null=True),
        ),
    ]
