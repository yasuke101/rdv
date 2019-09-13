from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from datetime import datetime,timedelta
from .models import *
from .forms import *
from .utils import render_to_pdf
from django.http import HttpResponse

def res_view(request):
	existed=None
	if request.method=='POST':
		form=res_form(request.POST,request.FILES)
		if form.is_valid():
			date=form.cleaned_data.get('date_de_RDV')
			date_max=(date+timedelta(minutes=15))
			date_min=(date-timedelta(minutes=15))
			if res.objects.filter(date_de_RDV__range=(date_min,date_max)).exists():
				messages.error(request,'La date est déja réservé')
				existed=res.objects.filter(date_de_RDV__date=date)
			else:
				cin=form.cleaned_data.get('CIN')
				nom=form.cleaned_data.get('nom')
				prenom=form.cleaned_data.get('prenom')
				telephone=form.cleaned_data.get('telephone')
				sexe=form.cleaned_data.get('sexe')
				#img_list=request.FILES.getlist('image_de_CIN')
				
				created=res.objects.create(date_de_RDV=date,CIN=cin,nom=nom,prenom=prenom,telephone=telephone,sexe=sexe)

				
				data={'data':created}
				pdf=render_to_pdf('pdf/rdv.html',data)
				return HttpResponse(pdf,content_type='application/pdf')
	else:
		form=res_form()
	return render(request,'core_templates/res.html',{'form': form,'existed':existed})
