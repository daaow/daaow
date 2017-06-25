#!/usr/bin/env python
# coding: utf-8

from django.contrib import admin
from django.contrib.sessions.models import Session


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        try:
            temp = obj.get_decoded().get('info')
            if temp:
                return temp
            else:
                raise KeyError
        except:
            return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']


admin.site.register(Session, SessionAdmin)

