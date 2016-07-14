from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

import option_price_calculator.views

urlpatterns = [
    url(r'^$', option_price_calculator.views.index, name='index'),
	url(r'^about', option_price_calculator.views.about, name='index'),
	url(r'^black_scholes', option_price_calculator.views.black_scholes, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
