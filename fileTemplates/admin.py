# -*- coding: utf-8 -*-
from django.contrib import admin

from hvad.admin import TranslatableAdmin
from opli.utils.admin import BaseAdmin

from .models import 

register = (,)

for item in register:
    admin.site.register(item, locals().get(item.__name__ + 'Admin', BaseAdmin))
