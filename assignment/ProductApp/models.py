from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class product_model(models.Model):
	name = models.CharField(max_length=256, blank=True, null=True)
	weight = models.BigIntegerField(null=True,blank=True)
	price = models.BigIntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name or '--Name not provided--'

	class Meta:
		verbose_name_plural = 'Product Model'
