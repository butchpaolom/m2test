from django.db import models

# Create your models here.

class People(models.Model):

    genders = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others")
    )

    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    middle_name = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(blank=True)
    gender = models.CharField(choices=genders, max_length=1, default='O')

    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"