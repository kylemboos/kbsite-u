from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^accounts/logout/$', 'django.contrib.auth.views.logout'), 
	(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}), 
	(r'^accounts/$', 'django.views.generic.simple.redirect_to', {'url': '/'}), 
	(r'^accounts/profile/$', 'django.views.generic.simple.redirect_to', {'url': '/'}),

    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

     url(r'^$', 'mysite.content.views.home', name='home'),
	 url(r'^blog/', 'mysite.content.views.blog', name='blog'),
	 url(r'^projects/', 'mysite.content.views.projects', name='projects'),
	 url(r'^resume/', 'mysite.content.views.resume', name='resume'),
	 url(r'^about/', 'mysite.content.views.about', name='about'),
	 url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': 'mysite/static/images/favicon.ico'}),
)
