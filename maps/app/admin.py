from django.contrib import admin

import csv
import codecs
from django.http import HttpResponseRedirect

from .models import Ordem, Maps

def importar_localidade(self, request, queryset):
	
	ordens = Ordem.objects.filter(pk__in=queryset)
	lista = list(ordens)

	for ordem in lista:

		dialect = csv.Sniffer().sniff(codecs.EncodedFile(ordem.file, "utf-8").read(1024))
		ordem.file.open()
		reader = csv.reader(codecs.EncodedFile(ordem.file, "utf-8"), delimiter=',', quotechar=';', dialect=dialect)
		
		for row in reader:
			
			line = row[0].split(';')

			m = Maps()
			if line[0] != "ID":
				print ' Salvando ... '
				m.identificador = line[0]
				m.latitude = line[1]
				m.longitude = line[2]
				m.location_type = line[3]
				m.locality = line[4]
				m.ordem = ordem
				m.save()

	self.message_user(request, "Importacao realizada.")

def editar_localidade(modeladmin, request, queryset):
	ordem = queryset[0]
	return HttpResponseRedirect("/list/?ordem=%s" % ordem.pk)

importar_localidade.short_description = "Importar localidades"
editar_localidade.short_description = "Editar localidades"

class MapsInline(admin.TabularInline):
    model = Maps

class OrdemAdmin(admin.ModelAdmin):
    list_display = ("titulo","data_criacao")
    inlines = (MapsInline,)
    actions = [importar_localidade, editar_localidade]

admin.site.register(Ordem, OrdemAdmin)
