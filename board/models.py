from __future__ import unicode_literals

from django.db import models
from Users.models import User
from datetime import datetime, date
# Create your models here.


class Board(models.Model):
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	title = models.TextField(max_length=255)
	content = models.TextField(max_length=255)
	parent = models.ForeignKey('board', null=True, blank=True)

	class Meta:
		verbose_name= ('board')
		ordering = ('-date',)

	def __str__(self):
		return self.title

	@staticmethod
	def get_boards(from_board=None):
		if from_board is not None:
			boards = Board.objects.filter(parent=None, id_lte=from_board)
		else:
			boards = Board.objects.filter(parent=None)
		return boards

	@staticmethod
	def get_board_after(board):
		#import pdb; pdb.set_trace()
		boards = Board.objects.filter(parent=None, id__gt=board)

		return boards