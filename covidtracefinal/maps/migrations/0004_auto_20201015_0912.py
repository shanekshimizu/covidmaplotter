# Generated by Django 3.1.2 on 2020-10-15 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_auto_20201015_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='thedoctor',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='thelocation',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
