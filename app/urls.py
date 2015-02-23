from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'app.views.home', name='home'),
    url(r'^directions', 'app.views.directions', name='directions'),
    url(r'^merchandise', 'app.views.merchandise', name='merchandise'),
    url(r'^tickets', 'app.views.tickets', name='tickets'),
    url(r'^schedule', 'app.views.schedule', name='schedule'),

    # url(r'^admin/', include(admin.site.urls)),
)
