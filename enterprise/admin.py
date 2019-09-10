# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from . models import Enterprise,Companies,Employee,Address

admin.site.register(Enterprise)
admin.site.register(Companies)
admin.site.register(Employee)
admin.site.register(Address)
