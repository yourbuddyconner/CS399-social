from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'app.views.splash', name='splash'),
    url(r'^feed', 'app.views.feed', name='feed'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^explore', 'app.views.explore', name='explore'),
    url(r'^dashboard', 'app.views.dashboard', name='dashboard'),
    url(r'^login', 'app.views.login', name='login'),
    url(r'^logout', 'app.views.logout', name='logout'),

    # url(r'^admin/', include(admin.site.urls)),
)
