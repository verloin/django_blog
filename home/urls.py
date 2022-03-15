from django.conf.urls import url
from django.urls import path, include

from home import views
from home.feeds import LatestPostsFeed
from home.views import AccountLogin

app_name = 'home'


urlpatterns = [
    url(r'^$', views.post_list, name='home'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    url('create_post/', views.PostCreateView.as_view(), name='create_post'),
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
    path('login/', AccountLogin.as_view(), name='login'),
]