# Generated by Django 3.1.7 on 2021-05-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210522_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='activation',
            name='address',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='activation',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
        ),
    ]