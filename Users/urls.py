from django.conf.urls import url
from django.contrib import admin
from Users import views

urlpatterns = [

	url(r'^$', views.listAllUser, name='list'),
	url(r'^add/', views.addUser, name='add'),
	url(r'^(?P<userId>\d+)/edit/', views.editUser, name='edit'),
	url(r'^(?P<val>\w+)/delete/', views.deleteUser, name='delete'),
	url(r'^create/', views.createUser, name='create'),
	url(r'^update/(?P<val>\w+)/?$', views.updateUser, name='update'),
	url(r'^downloadUserlist/', views.downloadUserlist, name='downloadUserlist'),
]
