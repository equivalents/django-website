from django.views.static import *
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *
from website.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  (r'^$', main_page),
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
  (r'^login/$', 'django.contrib.auth.views.login'),
  (r'^logout/$', logout_page),
  (r'^user/(\w+)/$', user_page),
  (r'^control/$', control_page),
  (r'^gpio_control/$', gpio_control_page),
  (r'^slider/$', slider_page),
  (r'^admin/', include(admin.site.urls)),
    
)
