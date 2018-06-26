from django import forms
from .models import data

class enteryForm(forms.ModelForm):

	class Meta:
		model=data
		fields=['Topic','Level','Question','Answer',]

	