from django_use_email_as_username.models import BaseUser, BaseUserManager
from datetime import date
from django.db import models


class User(BaseUser):
    objects = BaseUserManager()

    date_of_birth = models.DateField(null=True, blank=True)

    def calculate_age(self):
        today = date.today()
        birth_date = self.date_of_birth
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
