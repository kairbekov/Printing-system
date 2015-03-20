from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from mainapp import views


urlpatterns = [
    url(r'^persons/$', views.PersonList.as_view()),                         # get list of users
    url(r'^persons/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view()),        # get user by id
]

urlpatterns = format_suffix_patterns(urlpatterns)