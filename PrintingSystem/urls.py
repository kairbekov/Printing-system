from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mainapp/', include('mainapp.urls'))+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),                                       # main application
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),   # rest-framework
)
