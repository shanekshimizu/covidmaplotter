# Generated by Django 3.1.2 on 2020-10-29 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0048_auto_20201029_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='locations',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
