from django import forms
from django.utils import timezone
from datetime import datetime,time
from .models import *

class res_form(forms.ModelForm):
	date_de_RDV=forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
	class Meta:
		model=res
		fields=('date_de_RDV','CIN','nom','prenom','sexe','telephone')
	def clean_date_de_RDV(self):
		date=self.cleaned_data.get('date_de_RDV')

		date_day=date.strftime("%w")
		date_time=date.strftime("%X")

		if date and date<timezone.now():
			raise forms.ValidationError(u'La date est déja passer')
		else:
			if date_day=='0':
				raise forms.ValidationError(u'On est fermer les dimanches')
			elif date_day=='6':
				if date_time>time(hour=12, minute=0,second=0).strftime('%X') or date_time<time(hour=8, minute=0,second=0).strftime('%X'):
					raise forms.ValidationError(u"Pour le samedi les horaire de travail sont de 8:00 jusqu'a 12:00")
			elif date_time>time(hour=18, minute=0,second=0).strftime('%X') or date_time<time(hour=8, minute=0,second=0).strftime('%X'):
				raise forms.ValidationError(u"Les horaire de travail sont de 8:00 jusqu'a 18:00")
		return date		