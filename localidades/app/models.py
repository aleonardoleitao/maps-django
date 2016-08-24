# coding: utf-8

import os

from django.conf import settings
from django.db import models
from datetime import datetime
from get_username import get_username

class Ordem(models.Model):

    titulo = models.CharField("titulo", max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True)
    file = models.FileField(upload_to=settings.MEDIA_ROOT, blank = True)

    class Meta:
        ordering = ("data_criacao",)
        verbose_name = "localidade"
        verbose_name_plural = "Localidades"

    def __unicode__(self):
        return self.titulo

class Maps(models.Model):
    
    identificador = models.CharField(max_length=40)
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)
    location_type = models.CharField(max_length=40)
    locality = models.CharField(max_length=40)

    ordem = models.ForeignKey(Ordem, related_name="items")

    data_edicao = models.DateTimeField(null=True, blank=True)
    user_edicao = models.CharField(null=True, max_length=100)
    data_finalizacao = models.DateTimeField(null=True, blank=True)
    user_finalizacao = models.CharField(null=True, max_length=100)

    ANDAMENTO = 'A'
    ATUALIZADO = 'F'
    NAO_LOCALIZADO = 'X'
    NOVO = 'N'
    STATUS_CHOICES = (
        (ANDAMENTO, 'Andamento'),
        (ATUALIZADO, 'Atualizado'),
        (NAO_LOCALIZADO, 'Não Localizado'),
        (NOVO, 'Novo'),
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=NOVO,
    )

    class Meta:
        verbose_name = "maps"
        ordering = ("identificador",)

    def __unicode__(self):
        return self.identificador

    def atualiza(self, tipo):
        req = get_username()
        #if tipo = 'A':
        #else


