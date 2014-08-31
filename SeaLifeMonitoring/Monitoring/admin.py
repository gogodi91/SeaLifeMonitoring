from django.contrib import admin
from Monitoring.models import Area, Vessel, Cruise, Notes, Stations, TypeSpec, TAXA, ChemParam, Event, Chemistry, DataAB, SizeAgeFish, Age, Size

admin.site.register(Area)
admin.site.register(Vessel)
admin.site.register(Cruise)
admin.site.register(Notes)
admin.site.register(Stations)
admin.site.register(TypeSpec)
admin.site.register(TAXA)
admin.site.register(ChemParam)
admin.site.register(Event)
admin.site.register(Chemistry)
admin.site.register(DataAB)
admin.site.register(SizeAgeFish)
admin.site.register(Age)
admin.site.register(Size)


