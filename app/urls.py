from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from .signals import * #ensure that the signals are attatched via import
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

urlpatterns = patterns('app.views',
    # Examples:
    url(r'^error/', 'error', name='error'),
    url(r'^404/', '_404', name='404'),
    url(r'^$', 'index', name='index'),
    url(r'^create_customer/', 'create_customer', name='create_customer'),
    url(r'^charge_customer/', 'charge_customer', name='charge_customer'),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^survey', 'survey', name='survey'),
    url(r'^nutritionist/(?P<id>\d+)/$', 'nutritionist', name='nutritionist'),
    url(r'^recommended-nutritionists', 'recommended_nutritionists', name='recommended-nutritionists'),
    url(r'^schedule-consultation/(?P<id>\d+)/$', 'schedule_consultation', name='schedule-consultation'),
    url(r'^consultation/(?P<nutritionist_id>\d+)/(?P<consultation_id>\d+)/$', 'consultation', name='consultation'),
    url(r'^upcoming-consultations', 'upcoming_consultations', name='upcoming-consultations'),
    url(r'^my-nutritionists', 'my_nutritionists', name='my-nutritionists'),
    url(r'^about', 'about', name='about'),
    url(r'^terms', 'terms', name='terms'),
    url(r'^privacy', 'privacy', name='privacy'),
    url(r'^contact', 'contact', name='contact'),
)

def custom_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


urlpatterns += patterns('app.views', (r'^logout/$', custom_logout))
urlpatterns += patterns('app.views', (r'', include('account.urls')))
