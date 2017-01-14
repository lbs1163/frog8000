from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Message(models.Model):
	message_text = models.CharField(max_length=20)
	writer = models.CharField(max_length=5)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.message_text + " - " + self.writer