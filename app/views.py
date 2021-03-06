# Create your views here.
from decimal import *
from datetime import date

from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout

from django.conf import settings
from django.db.models import Q

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
from payments.models import Customer
from annoying.decorators import render_to, ajax_request

from .forms import StripeTokenForm, ChargeForm
from .models import HealthSurveyForm, ConsultationForm, Nutritionist, Credential, Demographic, Specialty, Availability, Consultation

from django.shortcuts import render, get_object_or_404

from django.core.urlresolvers import reverse

from django_mandrill.mail import MandrillTemplateMail

@render_to('index.html')
def index(request):
    return {}

@render_to('survey.html')
def survey(request):
   if request.method == 'POST':
      form = HealthSurveyForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect(reverse('recommended-nutritionists'))
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


def appointment_in_future(request):
   day = int(request.POST['date_day'])
   month = int(request.POST['date_month'])
   year = int(request.POST['date_year'])

   appointment = date(year, month, day)
   today = date.today()

   if appointment < today:
      return False
   else:
      return True


@render_to('schedule-consultation.html')
def schedule_consultation(request, id):
   nutritionist = Nutritionist.objects.get(id=id)
   availability = Availability.objects.filter(nutritionist=id)

   if request.method == 'POST':
      form = ConsultationForm(request.POST)
      print str(request.POST)

      if form.is_valid():
         if appointment_in_future(request):
            consultation = form.save(commit=False)
            consultation.user = request.user
            consultation.nutritionist = nutritionist
            consultation.save()
            return HttpResponseRedirect(reverse("consultation", args=(id, consultation.id)))
         else:
            form.error = "Consultation must occur in the future."
      else:
         form.error = "Invalid date and time."
   else:
      form = ConsultationForm()

   return { 'form': form,
            'nutritionist':nutritionist,
            'availability':availability[0],
            'user':request.user
          }


@render_to('consultation.html')
def consultation(request, nutritionist_id, consultation_id):

   nutritionist = Nutritionist.objects.get(id=nutritionist_id)
   availability = Availability.objects.filter(nutritionist=nutritionist_id)
   consultation = Consultation.objects.get(id=consultation_id)

   if consultation.user != request.user:
      return HttpResponseRedirect('/')

   stripe_price = int(nutritionist.consultation_price) * 100

   #import ipdb
   #ipdb.set_trace()

   if hasattr(request.user, 'customer'):
      print "TRUE user.customer: " + str(request.user.customer)
      user_has_stripe_account = True
   else:
      print "no stripe customer FALSE"
      user_has_stripe_account = False

   return { 'nutritionist':nutritionist,
            'availability':availability[0],
            'stripe_price':stripe_price,
            'consultation':consultation,
            'user_has_stripe_account':user_has_stripe_account
          }


@render_to('my-nutritionists.html')
def my_nutritionists(request):
   nutritionists = Nutritionist.objects.all()
   consultations = Consultation.objects.filter(user=request.user)

   for n in nutritionists:
      print str(n.id) + " " + str(n.headshot)

   return { 'nutritionists':nutritionists,
            'consultations':consultations
          }


@render_to('upcoming-consultations.html')
def upcoming_consultations(request):
   nutritionists = Nutritionist.objects.all()
   today = date.today()
   consultations = Consultation.objects.filter(Q(user=request.user) & Q(paid=True) & Q(date__gte=today))

   #import ipdb
   #ipdb.set_trace()

   for n in nutritionists:
      print str(n.id) + " " + str(n.headshot)

   return { 'nutritionists':nutritionists,
            'consultations':consultations
          }



'''
u'token[card][funding]': [u'credit'],
u'token[card][object]': [u'card'],
u'token[email]': [u'a@a.com'],
u'nutritionist': [u'1'],
u'token[card][address_line1]': [u''],
u'token[card][address_country]': [u''],
u'token[card][customer]': [u''],
u'token[type]': [u'card'],
u'token[created]': [u'1408395402'],
u'token[object]': [u'token'],
u'token[card][address_state]': [u''],
u'token[card][exp_year]': [u'2016'],
u'token[card][fingerprint]': [u'Xt5EWLLDS7FJjR1c'],
u'token[livemode]': [u'false'],
u'token[id]': [u'tok_14SxBG2eZvKYlo2CZg52LzcF'],
u'token[card][address_zip]': [u''],
u'token[card][country]': [u'US'],
u'token[card][exp_month]': [u'12'],
u'token[card][id]': [u'card_14SxBG2eZvKYlo2CbT2rHFfl'],
u'token[card][address_line2]': [u''],
u'token[used]': [u'false'],
u'token[card][last4]': [u'4242'],
u'token[card][brand]': [u'Visa'],
u'token[card][address_city]': [u''],
u'token[card][name]': [u'a@a.com']}>

request.POST['token[id]']
  u'tok_14SxBG2eZvKYlo2CZg52LzcF'
request.POST['token[card][id]']
  u'card_14SxBG2eZvKYlo2CbT2rHFfl'
'''

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
    print "charge_customer()"
    customer = request.user.customer
    print "customer: " + str(customer)

    form = ChargeForm(request.POST)
    print "form: " + str(form)

    if not form.is_valid():
        print "form not valid"
        return HttpResponseBadRequest()

    amount = form.cleaned_data['amount']
    print "amount: " + str(amount)
    customer.charge(amount, description="nutrifeedback")

    nutritionist_id = form.cleaned_data['nutritionist']
    print "n: " + str(nutritionist_id)

    consultation_id = form.cleaned_data['consultation']
    print "c: " + str(consultation_id)

    consultation = Consultation.objects.get(id=consultation_id)
    consultation.paid = True
    consultation.save()

    email_user(request, nutritionist_id, consultation_id)
    email_nutritionist(request, nutritionist_id, consultation_id)

    return HttpResponseRedirect("/")

    #IntegrityError: duplicate key value violates unique constraint "payments_customer_user_id_key"
    #DETAIL:  Key (user_id)=(1) already exists.


def email_user(request, nutritionist_id, consultation_id):
   current_site = get_current_site(request)
   domain = current_site.domain # not being set, is example.com

   email = request.user.email

   print str(current_site)
   print str(domain)

   consultation = get_object_or_404(Consultation, id=consultation_id)

   plain_body = render_to_string("user-email.txt", {"domain": domain, "consultation": consultation })
   html_body = render_to_string("user-email.html", {"domain": domain, "consultation": consultation })

   subject, from_email, to = 'Upcoming consultation', 'info@nutrifeedback.com', email
   text_content = plain_body
   html_content = html_body
   msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
   msg.attach_alternative(html_content, "text/html")
   #msg.content_subtype = "html" # with this gmail shows plain_body, link is clickable. Yahoo mail shows plain_body, link is not clickable
   msg.send()


def email_nutritionist(request, nutritionist_id, consultation_id):
   current_site = get_current_site(request)
   domain = current_site.domain # not being set, is example.com

   email = request.user.email

   print str(current_site)
   print str(domain)

   consultation = get_object_or_404(Consultation, id=consultation_id)

   plain_body = render_to_string("nutritionist-email.txt", {"domain": domain, "consultation": consultation })
   html_body = render_to_string("nutritionist-email.html", {"domain": domain, "consultation": consultation })

   subject, from_email, to = 'Upcoming consultation', 'info@nutrifeedback.com', email
   text_content = plain_body
   html_content = html_body
   msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
   msg.attach_alternative(html_content, "text/html")
   #msg.content_subtype = "html" # with this gmail shows plain_body, link is clickable. Yahoo mail shows plain_body, link is not clickable
   msg.send()
