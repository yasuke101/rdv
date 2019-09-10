from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import *
from .utils import render_to_pdf
from django.http import HttpResponse
import csv

class resadmin(admin.ModelAdmin):
	fieldsets=[
		('Information presonnelle',{'fields': [('nom','prenom','sexe'),('CIN','telephone')]}),
		('Information liée au métier',{'fields': ['date_de_RDV']}),
	]
	list_display=('CIN','nom','prenom','date_de_RDV','date_de_creation','telephone',)
	list_filter = ['date_de_RDV','date_de_creation']
	search_fields = ['CIN','nom','prenom','telephone']
	
	actions=["notice","attestation","export_as_csv"]
	
	def notice(self, request, queryset):
		data={'data':queryset.get()}
		pdf = render_to_pdf('pdf/notice.html',data)
		return HttpResponse(pdf,content_type='application/pdf')	
	notice.short_description = "Générer une ordonnance médicale"
	
	def attestation(self, request, queryset):
		data={'data':queryset.get()}
		pdf = render_to_pdf('pdf/attestation.html',data)
		return HttpResponse(pdf,content_type='application/pdf')
	attestation.short_description = "Générer une certificat médical"
	
	def export_as_csv(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)
		writer.writerow(field_names)
		for obj in queryset:
			row = writer.writerow([getattr(obj, field) for field in field_names])
		return response		
	export_as_csv.short_description = "Exporter les données dans un fichier Excel"

admin.site.register(res,resadmin)
admin.site.unregister(Group)


admin.site.index_title="Gestion des rendez-vous"
admin.site.site_title="Ici le nom du cabinet médical"
admin.site.site_header="Ici le nom / logo du cabinet médical"

