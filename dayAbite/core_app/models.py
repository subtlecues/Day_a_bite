from django.db import models

from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class BasalInsulin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dosage = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.TimeField()

class ShortTermInsulin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dosage = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.TimeField()

class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField()
    feeling = models.TextField()

class BitesSuggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_glucose_level = models.DecimalField(max_digits=5, decimal_places=2)
    bitess_amount = models.DecimalField(max_digits=5, decimal_places=2)

