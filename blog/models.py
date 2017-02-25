from __future__ import unicode_literals

from django.db import models
from Users.models import User
# Create your models here.


class Blog(models.Model):
	user = models.ForeignKey(User)
	title = models.TextField(max_length=255)
	content = models.TextField(max_length=255)
	parent = models.ForeignKey('Blog', null=True, blank=True)

	class Meta:
		verbose_name= ('Blog')

	def __str__(self):
		return self.title

	@staticmethod
	def get_blogs(from_blog=None):
		if from_blog is not None:
			blogs = Blog.objects.filter(parent=None, id_lte=from_blog)
		else:
			blogs = Blog.objects.filter(parent=None)
		return blogs

	@staticmethod
	def get_blog_after(blog):
		import pdb; pdb.set_trace()
		blogs = Blog.objects.filter(parent=None, id__gt=blog)

		return blogs