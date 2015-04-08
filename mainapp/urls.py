from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from mainapp import views
from mainapp.authentication import login_view, logout_view
from mainapp.views import home_view, login_page_view


urlpatterns = [
    url(r'^data/$', views.DataList.as_view()),                         #  get all documents
    url(r'^data/(?P<pk>[0-9]+)/$', views.DataDetail.as_view()),        # get document by id
    url(r'^users/$', views.UserList.as_view()),                        # get all users
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),       # get user by id
    url(r'^login/$', login_view),                                      # login request
    url(r'^logout/$', logout_view),                                    # logout request
    url(r'^home/$', home_view),                                        # home page
    url(r'^log-in/$', login_page_view),                                # log-in page
    url(r'^list/$', 'list', name='list'),


]

urlpatterns = format_suffix_patterns(urlpatterns)