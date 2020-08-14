from django import forms
from .models import *
from django.core.exceptions import ValidationError

class PostCreateForm(forms.ModelForm):

	class Meta:
		 model = Blog
		 fields = ['title','text', 'cover']


	def clean_slug(self):

		new_title = self.cleaned_data['title'].lower()

		if new_title == 'create':
			raise ValidationError('Title may not be "Create"')
		if Heading.objects.filter(title__iexact=new_title).count():
			raise ValidationError('Title "{}" must be unique'.format(new_title))

		return new_title