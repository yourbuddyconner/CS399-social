from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#from . import views


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'app.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'app.views.splash', name='splash'),
                       url(r'^feed', 'app.views.feed', name='feed'),
                       url(r'^about', 'app.views.about', name='about'),
                       url(r'^explore', 'app.views.explore', name='explore'),
                       url(r'^profile_picture', 'app.views.profile_picture',
                           name='profile_picture'),
                       url(r'^dashboard', 'app.views.dashboard',
                           name='dashboard'),
                       url(r'^login', 'app.views.login', name='login'),
                       url(r'^logout', 'app.views.logout', name='logout'),
                       # delete eventually
                       url(r'^temp', 'app.views.temp', name='temp'),
                       url(r'^posts', 'app.views.posts', name='posts'),
                       url(r'^admin/', include(admin.site.urls))
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
