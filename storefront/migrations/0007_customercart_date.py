# Generated by Django 4.0.3 on 2023-01-18 06:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0006_remove_customercheckout_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercart',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]