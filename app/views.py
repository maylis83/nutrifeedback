# Create your views here.
from decimal import *

from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.conf import settings

from django.contrib.auth.decorators import login_required

from payments.models import Customer
from annoying.decorators import render_to, ajax_request

from .forms import StripeTokenForm, ChargeForm
from .models import HealthSurveyForm, ConsultationForm, Nutritionist, Credential, Demographic, Specialty, Availability

from django.shortcuts import render
from django.http import HttpResponseRedirect


@render_to('index.html')
def index(request):
    return {}

@render_to('survey.html')
def survey(request):
   if request.method == 'POST':
      form = HealthSurveyForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/')
   else:
      form = HealthSurveyForm()

   return {'form': form, }


@render_to('recommended-nutritionists.html')
def recommended_nutritionists(request):
   nutritionists = Nutritionist.objects.all()

   for n in nutritionists:
      print str(n.id) + " " + str(n.headshot)

   return { 'nutritionists':nutritionists }


@render_to('nutritionist.html')
def nutritionist(request, id):

   nutritionist = Nutritionist.objects.get(id=id)

   print "nutritionist headshot: " + str(nutritionist.headshot)

   credentials = Credential.objects.filter(nutritionist=id)
   degrees = credentials.filter(type='degree')
   licenses = credentials.filter(type='license')
   courses = credentials.filter(type='course')
   demographics = Demographic.objects.filter(nutritionist=id)
   specialties = Specialty.objects.filter(nutritionist=id)
   availability = Availability.objects.filter(nutritionist=id)

   #import ipdb
   #ipdb.set_trace()

   return { 'nutritionist':nutritionist,
            'degrees':degrees,
            'licenses':licenses,
            'courses':courses,
            'demographics':demographics,
            'specialties':specialties,
            'availability':availability[0] }


@render_to('schedule-consultation.html')
def schedule_consultation(request, id):
   if request.method == 'POST':
      form = ConsultationForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/')
   else:
      form = HealthSurveyForm()

   nutritionist = Nutritionist.objects.get(id=id)
   availability = Availability.objects.filter(nutritionist=id)

   return { 'form': form,
            'nutritionist':nutritionist,
            'availability':availability[0]
          }


@render_to('consultation.html')
def consultation(request, id):

   nutritionist = Nutritionist.objects.get(id=id)
   availability = Availability.objects.filter(nutritionist=id)

   return { 'nutritionist':nutritionist,
            'availability':availability[0] }


@render_to('my-nutritionists.html')
def my_nutritionists(request):
   nutritionists = Nutritionist.objects.all()

   for n in nutritionists:
      print str(n.id) + " " + str(n.headshot)

   return { 'nutritionists':nutritionists }


@render_to('upcoming-consultations.html')
def upcoming_consultations(request):
   nutritionists = Nutritionist.objects.all()

   for n in nutritionists:
      print str(n.id) + " " + str(n.headshot)

   return { 'nutritionists':nutritionists }



def error(request):
    """for testing purposes"""
    raise Exception

def _404(request):
    """for testing purposes"""
    raise Http404

@ajax_request
@login_required
def create_customer(request):
    form = StripeTokenForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()
    card = form.cleaned_data['id']
    customer = Customer.create(request.user, card=card, charge_immediately=False)
    return {}

@login_required
def charge_customer(request):
    customer = request.user.customer
    form = StripeTokenForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()

    amount = form.cleaned_data['amount']
    customer.charge(amount, description="nutrifeedback")
    return HttpResponseRedirect("/")
