# Generated by Django 3.1.2 on 2020-10-19 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0022_auto_20201019_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='thepatients',
            new_name='patients',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='locations',
        ),
        migrations.AddField(
            model_name='patient',
            name='locations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_location', to='maps.location'),
        ),
    ]
