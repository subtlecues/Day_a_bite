from django.contrib import admin
from .models import InsulinShot, Measurement, BitesConsumedEntry


class InsulinShotAdmin(admin.ModelAdmin):
    pass

class MeasurementAdmin(admin.ModelAdmin):
    pass

class BitesConsumedEntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(InsulinShot, InsulinShotAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(BitesConsumedEntry, BitesConsumedEntryAdmin)
