from django import forms
from .models import *

class user_post_form(forms.ModelForm):
	class Meta:
		model = post_model
		fields = ('text',)