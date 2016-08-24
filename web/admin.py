from django.contrib import admin
from .models import Sport, Athlete, ScheduleItem, VisitRegistry


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('identification', 'first_name', 'last_name', 'weight', 'sport', )
    search_fields = ('first_name', )
    list_filter = ('sport', )
    list_editable = ('first_name', 'sport',)


@admin.register(ScheduleItem)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('state', 'result', 'modality', 'sport', 'athlete', 'datetime',)
    search_fields = ('state', )
    list_filter = ('sport','result', 'datetime',)
    list_editable = ('sport','result', 'datetime',)


@admin.register(VisitRegistry)
class VisitRegistry(admin.ModelAdmin):
    list_display = ('datetime','user_type', )
    search_fields = ('user_type', )



