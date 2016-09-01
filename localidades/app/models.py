# coding: utf-8

import os

from django.conf import settings
from django.db import models
from datetime import datetime
from get_username import get_username
from datetime import datetime

class Ordem(models.Model):

    titulo = models.CharField("titulo", max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True)
    file = models.FileField(upload_to=settings.MEDIA_ROOT, blank = True)

    SHOW = 'S'
    SHOW_EDITABLE = 'E'
    HIDE = 'H'

    SHOW_X_EDITABLE = (
        (SHOW, 'Show'),
        (SHOW_EDITABLE, 'Show Editable'),
    )
    SHOW_X_HIDE = (
        (SHOW, 'Show'),
        (HIDE, 'Hide'),
    )

    exibe_identificador = models.CharField(
        max_length=1,
        choices=SHOW_X_HIDE,
        default=SHOW,
    )

    exibe_address = models.CharField(
        max_length=1,
        choices=SHOW_X_EDITABLE,
        default=SHOW,
    )

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
    address = models.CharField(max_length=1024, null=True, blank=True)

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

    def atualiza(self, tipo, usuario):

        if tipo == Maps.ANDAMENTO:
            self.status = Maps.ANDAMENTO
            self.data_edicao = datetime.now()
            self.user_edicao = usuario
            self.save()

        elif tipo == Maps.ATUALIZADO:
            self.status = Maps.ATUALIZADO
            self.data_finalizacao = datetime.now()
            self.user_finalizacao = usuario
            self.save()

        elif tipo == Maps.NAO_LOCALIZADO:
            self.status = Maps.NAO_LOCALIZADO
            self.data_finalizacao = datetime.now()
            self.user_finalizacao = usuario
            self.latitude = 0
            self.longitude = 0
            self.save()

        else:
            self.status = Maps.NOVO
            self.save()