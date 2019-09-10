
from django.contrib import admin

from . models import Enterprise,Company,Employee,Address

admin.site.register(Enterprise)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Address)