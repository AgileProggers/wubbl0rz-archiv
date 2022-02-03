# Generated by Django 4.0.2 on 2022-02-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broadcaster_id', models.SlugField(default='108776574')),
                ('ttv_client_id', models.SlugField()),
                ('ttv_client_secret', models.SlugField()),
                ('ttv_bearer_token', models.SlugField(blank=True, null=True)),
                ('date_vods_updated', models.DateTimeField(blank=True, null=True)),
                ('date_emotes_updated', models.DateTimeField(blank=True, null=True)),
                ('is_live', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emote',
            fields=[
                ('id', models.SlugField(primary_key=True, serialize=False)),
                ('name', models.SlugField()),
                ('url', models.URLField()),
                ('provider', models.SlugField()),
                ('outdated', models.BooleanField(default=False)),
            ],
        ),
    ]
