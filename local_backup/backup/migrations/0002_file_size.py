# Generated by Django 3.2.9 on 2021-11-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]