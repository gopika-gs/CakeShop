# Generated by Django 4.0.3 on 2023-01-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0023_remove_customercart_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercart',
            name='message',
            field=models.CharField(default=None, max_length=40),
        ),
    ]