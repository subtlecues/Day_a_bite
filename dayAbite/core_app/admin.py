from django.contrib import admin
from .models import InsulinShot, BloodGlucoseMeasurement, BitesConsumedEntry


class InsulinShotAdmin(admin.ModelAdmin):
    list_display = ('user', 'insulin_type', 'dosage', 'created_at', 'updated_at')

class BloodGlucoseMeasurementAdmin(admin.ModelAdmin):
    list_display = ('user', 'value', 'feeling', 'created_at', 'updated_at')

class BitesConsumedEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'bites_amount', 'created_at', 'updated_at')


admin.site.register(InsulinShot, InsulinShotAdmin)
admin.site.register(BloodGlucoseMeasurement, BloodGlucoseMeasurementAdmin)
admin.site.register(BitesConsumedEntry, BitesConsumedEntryAdmin)
