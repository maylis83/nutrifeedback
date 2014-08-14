from django.db import models
from django_extensions.db.models import AutoSlugField
from model_utils.models import TimeStampedModel
from django.forms import ModelForm, Textarea, TextInput, Select
from django.forms.extras.widgets import SelectDateWidget
from util.util import file_url

class Nutritionist(TimeStampedModel):

   NUTRITIONIST_TYPES = (
       ('dietician' , 'Registered Dietician'),
       ('certified_nutrition_specialist' , 'Certified nutrition specialist'),
       ('certified_clinical_nutritionist' , 'Certified clinical nutritionist'),
       ('diplomat' , 'Diplomat of the American Clinical Board of Nutrition'),
       ('holistic_nutritionist' , 'Holistic nutritionist'),
       ('certified_health_coach' , 'Certified health coach'),
       ('certified_nutritionist' , 'Certified nutritionist'),
       ('certified_nutrition_consultant' , 'Certified nutrition consultant'),
     )

   MEETING_TYPES = (
       ('in_person' , 'In Person'),
       ('phone_call' , 'Phone Call'),
       ('video_call' , 'Video Call'),
     )

   first_name = models.CharField(max_length=255)
   last_name = models.CharField(max_length=255)
   nutritionist_type = models.CharField(max_length=255, choices=NUTRITIONIST_TYPES)
   meeting_type = models.CharField(max_length=255, choices=MEETING_TYPES)
   tag_phrase = models.CharField(max_length=2048)
   address = models.CharField(max_length=255)
   city = models.CharField(max_length=255)
   state = models.CharField(max_length=255)
   zip = models.CharField(max_length=255)
   users = models.ManyToManyField('account.User', related_name='nutritionist_users', null=True, blank=True)
   consultation_description = models.CharField(max_length=4096)
   skype_name = models.CharField(max_length=255)
   headshot = models.ImageField(upload_to=file_url("/nutritionist_headshots"), default='/nutritionist_headshots/none.jpg')
   consultation_price = models.IntegerField()

   def get_full_name(self):
        return unicode(self.first_name) + " " + unicode(self.last_name)

   def __unicode__(self):
        return self.get_full_name()


class Consultation(TimeStampedModel):
   user = models.ForeignKey('account.User', related_name='user_consultation', null=True, blank=True)
   nutritionist = models.ForeignKey('Nutritionist', related_name='nutritionist_consultation', null=True, blank=True)
   consultation = models.DateTimeField()

   def __unicode__(self):
        return self.user.get_full_name() + " and " + self.nutritionist.get_full_name() + " on " + unicode(self.consultation)


class Credential(TimeStampedModel):
   CREDENTIAL_TYPE = (
      ('degree', 'Degree'),
      ('license', 'License'),
      ('course', 'Course'),
   )

   type = models.CharField(max_length=255, choices=CREDENTIAL_TYPE)
   description = models.CharField(max_length=1024)
   nutritionist = models.ManyToManyField('Nutritionist', related_name='nutritionist_credential', null=True, blank=True)

   def __unicode__(self):
        #return self.nutritionist.get_full_name() + unicode(self.type) + " " + unicode(self.description)
        return unicode(self.type) + " " + unicode(self.description)

class Demographic(TimeStampedModel):
   DEMOGRAPHIC_TYPE = (
      ('adult', 'Adult'),
      ('senior', 'Senior'),
      ('christian', 'Christian'),
      ('muslim', 'Muslim'),
      ('jewish', 'Jewlish'),
      ('buddhists', 'Buddhists'),
      ('african_american', 'African American'),
      ('latino_american', 'Latino American'),
      ('asian_american', 'Asian American'),
   )

   type = models.CharField(max_length=255, choices=DEMOGRAPHIC_TYPE)
   nutritionist = models.ManyToManyField('Nutritionist', related_name='nutritionist_demographic', null=True, blank=True)

   def __unicode__(self):
        return unicode(self.type)


class Specialty(TimeStampedModel):
   SPECIALTY_TYPE = (
      ('anger_management', 'Anger Management'),
      ('aspergers', 'Asperger\'s'),
      ('divorce', 'Divorce'),
      ('domestic_violence', 'Domestic Violence'),
      ('relationships', 'Relationships'),
      ('spirituality', 'Spirituality'),
      ('stress', 'Stress'),
   )

   type = models.CharField(max_length=255, choices=SPECIALTY_TYPE)
   nutritionist = models.ManyToManyField('Nutritionist', related_name='nutritionist_specialty', null=True, blank=True)

   def __unicode__(self):
        return unicode(self.type)


class Availability(TimeStampedModel):

   monday_early = models.BooleanField(default=False)
   monday_afternoon = models.BooleanField(default=False)
   monday_evening = models.BooleanField(default=False)

   tuesday_early = models.BooleanField(default=False)
   tuesday_afternoon = models.BooleanField(default=False)
   tuesday_evening = models.BooleanField(default=False)

   wednesday_early = models.BooleanField(default=False)
   wednesday_afternoon = models.BooleanField(default=False)
   wednesday_evening = models.BooleanField(default=False)

   thursday_early = models.BooleanField(default=False)
   thursday_afternoon = models.BooleanField(default=False)
   thursday_evening = models.BooleanField(default=False)

   friday_early = models.BooleanField(default=False)
   friday_afternoon = models.BooleanField(default=False)
   friday_evening = models.BooleanField(default=False)

   saturday_early = models.BooleanField(default=False)
   saturday_afternoon = models.BooleanField(default=False)
   saturday_evening = models.BooleanField(default=False)

   sunday_early = models.BooleanField(default=False)
   sunday_afternoon = models.BooleanField(default=False)
   sunday_evening = models.BooleanField(default=False)

   nutritionist = models.ForeignKey('Nutritionist', related_name='nutritionist_availability', null=True, blank=True)

   def __unicode__(self):
        return ("  M " + unicode(self.monday_early) + " " + unicode(self.monday_afternoon) + " " + unicode(self.monday_evening) + " " + \
   "  T " + unicode(self.tuesday_early) + " " +  unicode(self.tuesday_afternoon) + " " + unicode(self.tuesday_evening) + " " + \
   "  W " + unicode(self.wednesday_early) + " " + unicode(self.wednesday_afternoon) + " " + unicode(self.wednesday_evening) + " " + \
   "  TR " + unicode(self.thursday_early) + " " + unicode(self.thursday_afternoon) + " " + unicode(self.thursday_evening) + " " + \
   "  F " + unicode(self.friday_early) + " " + unicode(self.friday_afternoon) + " " + unicode(self.friday_evening) + " " + \
   "  S " + unicode(self.saturday_early) + " " + unicode(self.saturday_afternoon) + " " + unicode(self.saturday_evening) + " " + \
   "  S " + unicode(self.sunday_early) + " " + unicode(self.sunday_afternoon) + " " + unicode(self.sunday_evening))


class HealthSurvey(TimeStampedModel):
   GENDER = (('male', 'Male'), ('female', 'Female'))
   EXERCISE_FREQ = [(str(i),str(i)) for i in range(26)]
   HEALTH_GOALS = (('dummy','dummy'),)
   DIETARY_RESTRICTIONS = (('dummy','dummy'),)

   gender = models.CharField(max_length=10, choices=GENDER, verbose_name='gender')
   dob = models.DateField(verbose_name='When is your date of birth?')
   weight = models.IntegerField(verbose_name='weight')
   height = models.CharField(max_length=10, verbose_name='height')
   exercise_freq = models.CharField(max_length=255, choices=EXERCISE_FREQ, verbose_name='how often do you exercise per week?')
   health_goals = models.CharField(max_length=255, choices=HEALTH_GOALS, verbose_name='what are your health goals?')
   dietary_restrictions = models.CharField(max_length=255, choices=DIETARY_RESTRICTIONS, verbose_name='do you have any dietary restrictions?')
   anything_else = models.CharField(max_length=4096, null=True, blank=True, verbose_name='anything else you would like us to know:')

   def __unicode__(self):
        return unicode(self.gender) + " " + unicode(self.dob)



'''
class (TimeStamp edModel):
   def __unicode__(self):
        return unicode(self.)
'''

class HealthSurveyForm(ModelForm):


   class Meta:
      BIRTH_YEAR_CHOICES = [str(i + 1915) for i in range(100)]
      model = HealthSurvey
      fields = ['gender', 'dob', 'weight', 'height', 'exercise_freq', 'health_goals', 'dietary_restrictions', 'anything_else']
      widgets = {
          'anything_else': Textarea(attrs={'cols':100, 'rows':10, 'class':'form-field'}),
          'weight': TextInput(attrs={'class':'form-field form-field-height-weight-size'}),
          'height': TextInput(attrs={'class':'form-field form-field-height-weight-size'}),
          'exercise_freq': Select(attrs={'class':'form-field form-field-dropdown-size'}),
          'health_goals': Select(attrs={'class':'form-field form-field-dropdown-size'}),
          'dietary_restrictions': Select(attrs={'class':'form-field form-field-dropdown-size'}),
          'gender': Select(attrs={'class':'form-field form-field-gender-size'}),
          'dob':SelectDateWidget(attrs={'class':'form-field form-field-dob-size'}, years=BIRTH_YEAR_CHOICES),
      }
