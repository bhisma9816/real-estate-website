# Generated by Django 2.1 on 2019-05-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bedroom',
            field=models.IntegerField(),
        ),
    ]
