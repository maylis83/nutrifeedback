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
   extra = 1
   max_num = 5


class NutritionistAdmin(admin.ModelAdmin):
   inlines = [
      AvailabilityInline,
      CredentialInline
   ] # These are not showing up at all, but the code is being eval, wtf?

admin.site.register(Nutritionist, NutritionistAdmin)
