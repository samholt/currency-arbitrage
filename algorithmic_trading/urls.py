from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

import currency_arbitrage.views

urlpatterns = [
    url(r'^$', currency_arbitrage.views.index, name='index'),
	url(r'^about', currency_arbitrage.views.about, name='index'),
]
