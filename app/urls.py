from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView


urlpatterns = patterns('app.views',
    # Examples:
    url(r'^error/', 'error', name='error'),
    url(r'^404/', '_404', name='404'),
    url(r'^$', 'index', name='index'),
    url(r'^create_customer/', 'create_customer', name='create_customer'),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^survey', 'survey', name='survey'),
    url(r'^nutritionist/(?P<id>\d+)/$', 'nutritionist', name='nutritionist'),
    url(r'^recommended-nutritionists', 'recommended_nutritionists', name='recommended-nutritionists')
)

from .signals import * #ensure that the signals are attatched via import
urlpatterns += patterns('app.views', (r'', include('account.urls')))
