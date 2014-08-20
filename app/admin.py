from django.contrib import admin
from models import Nutritionist, Consultation, Credential, Demographic, Specialty, Availability, HealthSurvey
import reversion

admin.site.register(Consultation)
admin.site.register(Credential)
admin.site.register(Demographic)
admin.site.register(Specialty)
admin.site.register(Availability)
admin.site.register(HealthSurvey)


class AvailabilityInline(admin.StackedInline):
   model = Availability
   extra = 1
   max_num = 1


class CredentialInline(admin.StackedInline):
   model = Credential.nutritionist.through
   Credential.nutritionist.through.__unicode__ = lambda x: ''
   extra = 5
   max_num = 15
   verbose_name = "Credential"
   verbose_name_plural = "Credentials"

class DemographicInline(admin.StackedInline):
   model = Demographic.nutritionist.through
   Demographic.nutritionist.through.__unicode__ = lambda x: ''
   extra = 5
   max_num = 15
   verbose_name = "Demographic"
   verbose_name_plural = "Demographics"


class SpecialtyInline(admin.StackedInline):
   model = Specialty.nutritionist.through
   Specialty.nutritionist.through.__unicode__ = lambda x: ''
   extra = 5
   max_num = 15
   verbose_name = "Specialty"
   verbose_name_plural = "Specialties"


class NutritionistAdmin(admin.ModelAdmin):
   inlines = [
      AvailabilityInline,
      CredentialInline,
      DemographicInline,
      SpecialtyInline
   ]

admin.site.register(Nutritionist, NutritionistAdmin)
