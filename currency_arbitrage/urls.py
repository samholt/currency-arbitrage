# app specific urls
from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^index', 'currency_arbitrage.views.home'),
)
