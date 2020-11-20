from django.db import models

#Create your models here. (for database)
#run python3 manage.py makemigrations after creating classes, then run python3 manage.py migrate
#then go to admin and put in register


class Doctor(models.Model):
    name = models.CharField(max_length = 300, null = True)
    phone = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    HOSPITALS = (
        ('Adventist Health Castle', 'Adventist Health Castle'),
        ('Hawaii State Hospital', 'Hawaii State Hospital'),
        ('Kahuku Medical Center', 'Kahuku Medical Center'),
        ('Pali Momi Medical Center', 'Pali Momi Medical Center'),
        ('The Queens Medical Center-Ewa Beach', 'The Queens Medical Center-Ewa Beach'),
        ('Wahiawa General Hospital', 'Wahiawa General Hospital'),
        ('Kaiser Permanente Moanalua Medical Center', 'Kaiser Permanente Moanalua Medical Center'),
        ('Kapiolani Medical Center for Women & Children', 'Kapiolani Medical Center for Women & Children'),
        ('Kuakini Medical Center', 'Kuakini Medical Center'),
        ('The Queens Medical Center', 'The Queens Medical Center'),
        ('Shriners Hospital for Children', 'Shriners Hospital for Children'),
        ('Straub Clinic & Hospital', 'Straub Clinic & Hospital'),
        ('Tripler Army Medical Center', 'Tripler Army Medical Center'),

    )

    name = models.CharField(max_length = 300, null = True, choices = HOSPITALS)
    bed_count = models.IntegerField(null = True)

    def __str__(self):
        return self.name


class Location(models.Model):
    CITIES = (
        ('Honolulu', 'Honolulu'),
        ('Ewa Beach', 'Ewa Beach'),
        ('Kailua', 'Kailua'),
        ('Mililani', 'Mililani'),
        ('Waianae', 'Waianae'),
        ('Waipahu', 'Waipahu'),
        ('Peal City', 'Pearl City'),
        ('Kapolei', 'Kapolei'),
        ('Kakoako', 'Kakoako'),

    )

    LOC_TYPES = (
        ('Hotel', 'Hotel'),
        ('Restaurant', 'Restaurant'),
        ('Bar', 'Bar'),
        ('Retail', 'Retail'),
        ('Gym', 'Gym'),
        ('Industrial', 'Industrial'),
        ('Business', 'Business'),
    )
    address = models.CharField(max_length = 300, null = True)
    latitude = models.CharField(max_length = 300, null = True)
    longitude = models.CharField(max_length = 300, null = True)
    city = models.CharField(max_length = 300, null = True, choices = CITIES)
    loc_type = models.CharField(max_length = 300, null = True, choices = LOC_TYPES)
    cooldown = models.CharField(max_length = 50, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.address

#reverse query - location.patient_set.all()
class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, null = True, blank = True, on_delete = models.SET_NULL)
    hospital = models.ForeignKey(Hospital, null = True, blank = True, on_delete = models.SET_NULL)
    locations = models.ManyToManyField(Location, blank = True)
    firstname = models.CharField(max_length = 300, null = True)
    lastname = models.CharField(max_length = 300, null = True)
    birthday = models.CharField(max_length = 200, null = True)
    address = models.CharField(max_length = 300, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 300, null = True)
    cooldown = models.CharField(max_length = 50, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)