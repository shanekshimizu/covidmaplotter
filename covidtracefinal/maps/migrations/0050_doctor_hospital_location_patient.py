# Generated by Django 3.1.2 on 2020-10-29 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maps', '0049_auto_20201029_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Adventist Health Castle', 'Adventist Health Castle'), ('Hawaii State Hospital', 'Hawaii State Hospital'), ('Kahuku Medical Center', 'Kahuku Medical Center'), ('Pali Momi Medical Center', 'Pali Momi Medical Center'), ('The Queens Medical Center-Ewa Beach', 'The Queens Medical Center-Ewa Beach'), ('Wahiawa General Hospital', 'Wahiawa General Hospital'), ('Kaiser Permanente Moanalua Medical Center', 'Kaiser Permanente Moanalua Medical Center'), ('Kapiolani Medical Center for Women & Children', 'Kapiolani Medical Center for Women & Children'), ('Kuakini Medical Center', 'Kuakini Medical Center'), ('The Queens Medical Center', 'The Queens Medical Center'), ('Shriners Hospital for Children', 'Shriners Hospital for Children'), ('Straub Clinic & Hospital', 'Straub Clinic & Hospital'), ('Tripler Army Medical Center', 'Tripler Army Medical Center')], max_length=300, null=True)),
                ('bed_count', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300, null=True)),
                ('latitude', models.CharField(max_length=300, null=True)),
                ('longitude', models.CharField(max_length=300, null=True)),
                ('city', models.CharField(choices=[('Honolulu', 'Honolulu'), ('Ewa Beach', 'Ewa Beach'), ('Kailua', 'Kailua'), ('Mililani', 'Mililani'), ('Waianae', 'Waianae'), ('Waipahu', 'Waipahu'), ('Peal City', 'Pearl City'), ('Kapolei', 'Kapolei'), ('Kakoako', 'Kakoako')], max_length=300, null=True)),
                ('loc_type', models.CharField(choices=[('Hotel', 'Hotel'), ('Restaurant', 'Restaurant'), ('Bar', 'Bar'), ('Retail', 'Retail'), ('Gym', 'Gym'), ('Industrial', 'Industrial'), ('Business', 'Business')], max_length=300, null=True)),
                ('cooldown', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=300, null=True)),
                ('lastname', models.CharField(max_length=300, null=True)),
                ('birthday', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=300, null=True)),
                ('cooldown', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maps.doctor')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maps.hospital')),
                ('locations', models.ManyToManyField(blank=True, to='maps.Location')),
            ],
        ),
    ]
