from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'admin/login.html'}, name='login'),
    url(r'^auth/', include('authenticated.urls')),

    (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^balanced/', include('balanced.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
