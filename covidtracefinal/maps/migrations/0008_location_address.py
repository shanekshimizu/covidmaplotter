# Generated by Django 3.1.2 on 2020-10-17 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0007_auto_20201015_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
