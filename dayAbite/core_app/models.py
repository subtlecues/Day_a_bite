from datetime import datetime
from django.db.models import Model, ForeignKey, DateTimeField, DecimalField, TextField, CASCADE, CharField
from custom_user.models import User



class TimeStampedModel(Model):
    """
    An abstract base class model that provides self-updating
    `created_at` and `updated_at` fields.
    """

    created_at = DateTimeField(auto_now_add=True )
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-updated_at"]
        get_latest_by = "-updated_at"

class InsulinShot(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE, related_name='user_insulin_shots')
    INSULIN_TYPE_CHOICES = [
        ('Short-term', 'Short-term, fast-acting insulin'),
        ('Basal', 'Basal, long-term acting insulin')
    ]
    insulin_type = CharField(max_length=20, choices=INSULIN_TYPE_CHOICES, null=True)
    dosage = DecimalField(max_digits=5, decimal_places=2)

    


class Measurement(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE, related_name='user_measurements')
    value = DecimalField(max_digits=5, decimal_places=2)
    feeling = TextField()


class BitesConsumedEntry(TimeStampedModel):
    """One Bite equals 10 carbs intake."""
    user = ForeignKey(User, on_delete=CASCADE, related_name='bites_consumed_entries')
    bites_amount = DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.username}'s Carbs Entry - {self.created_at}"