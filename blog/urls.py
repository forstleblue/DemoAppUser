from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.bloghome, name='blog'),
    url(r'^post/$', views.createBlog, name='post'),
    url(r'^remove/$', views.remove, name='remove'),
]