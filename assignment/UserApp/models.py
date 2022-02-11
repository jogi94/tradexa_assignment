from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class post_model(models.Model):
	user = models.ForeignKey(User, related_name='userPM', on_delete=models.SET_NULL, blank=True, null=True)
	text = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.text or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Post Model'
