# coding: utf-8
#-*- encoding=utf-8 -*-

import traceback
import sys
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed, HttpResponseForbidden
import simplejson
import commands
from django.views.decorators.csrf import csrf_exempt
from django.db import connection, transaction
from django.shortcuts import render, render_to_response
from django.conf import settings
from django.views.decorators.cache import never_cache
import csv
import codecs
from models import Ordem, Maps
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def index(request):
        return render(request,'index.html')

def upload(request):
    if request.POST and request.FILES:

		csvfile = request.FILES['csv_file']
		dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
		csvfile.open()
		reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', quotechar=';', dialect=dialect)
		titulo  = request.POST["titulo"]
		
		ordem = Ordem()
		ordem.titulo = titulo
		ordem.save()

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
				print ' Salvo - ' + m.identificador
        
    return render(request, "upload.html", locals())

def list(request):

	if not request.user.is_authenticated():
		return HttpResponseRedirect('/admin/login/?next=/admin/app/ordem/')

	r = request.GET
	rg = request.GET.get

	ident = 0
	pagina = ''

	if r.has_key('ordem') and rg('ordem') != '':
		ident = rg('ordem')

	if r.has_key('pagina') and rg('pagina') != '':	
		pagina = rg('pagina')

	try:
		ident = int(ident)
	except ValueError:
		return HttpResponseBadRequest(_('ID is not numeric'))

	#import ipdb
	#ipdb.set_trace()

	lista = Maps.objects.filter(ordem=ident).order_by('pk')
	paginator = Paginator(lista, 1)
	proximo = ''
	atual = ''
	anterior = ''

	if pagina != '':
		pg_atual = paginator.page(pagina)
		atual = pg_atual[0]
		if pg_atual.has_previous():
			anterior = int(pagina) - 1
		if pg_atual.has_next():
			proximo = int(pagina) + 1
	else:
		pg_atual = paginator.page(1)
		atual = pg_atual[0]
		if pg_atual.has_next():
			proximo = 2

	usuario = ""
	if request.user != None:
		usuario = request.user.username

	if atual != '' and atual != None:
		atual.atualiza(Maps.ANDAMENTO, usuario)

	data = {
		'anterior': anterior,
		'proximo': proximo,
		'atual': atual,
		'ordem': ident		
    }

	#return render(request,'list.html')
	return render_to_response('list.html', data)

@csrf_exempt
def gravar(request):

	ID = request.POST["id"]
	identificador = request.POST["identificador"]
	latitude = request.POST["latitude"]
	longitude = request.POST["longitude"]
	tipo = request.POST["tipo"]
	mensagem = ""

	usuario = ""
	if request.user != None:
		usuario = request.user.username

	try:
		maps = Maps.objects.get(id=ID)
		maps.latitude = latitude
		maps.longitude = longitude
		maps.atualiza(tipo, usuario)
		mensagem = "Corrigida a localização"

	except Exception, exception:
		mensagem = "Erro ao atualizar o registro"

	return HttpResponse(mensagem)

def atualizar(request):
	ident = request.GET["identificador"]
	maps = Maps.objects.get(identificador=ident)

	jsonData = {}
	jsonData['identificador'] = maps.identificador
	jsonData['latitude'] = maps.latitude
	jsonData['longitude'] = maps.longitude

	return HttpResponse(simplejson.dumps(jsonData))