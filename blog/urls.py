from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from home.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]
