from django.conf.urls import url

from board import views

urlpatterns = [
    url(r'^$', views.boardhome, name='board'),
    url(r'^createboard/$', views.createboard, name='createboard'),
    url(r'^remove/$', views.remove, name='remove'),
    url(r'^(?P<boardid>\d+)/$', views.detailBoard, name='detailBoard'), 
]