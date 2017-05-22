from django.contrib import admin

from .models import Booking , Area , Bar , Drink 

class BookingAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Booking._meta.fields]
		
admin.site.register(Booking,BookingAdmin)

class AreaAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Area._meta.fields]
		
admin.site.register(Area,AreaAdmin)

class BarAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Bar._meta.fields]
		
admin.site.register(Bar,BarAdmin)

class DrinkAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Drink._meta.fields]
		
admin.site.register(Drink,DrinkAdmin)


