# Generated by Django 3.2.14 on 2022-07-29 03:30

from django.db import migrations, models
import trasia_watches_store.models


class Migration(migrations.Migration):

    dependencies = [
        ('trasia_watches_store', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='wimage',
            field=models.ImageField(blank=True, null=True, upload_to=trasia_watches_store.models.upload_to, verbose_name='Watch Image'),
        ),
    ]