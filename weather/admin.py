from django.contrib import admin

from weather.models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(City, CityAdmin)
