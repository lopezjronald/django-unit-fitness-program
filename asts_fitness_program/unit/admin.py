from django.contrib import admin
from .models import Fitness_Level, Airman, Physical_Training_Leader, Profile, Failure, Unit_Fitness_Program_Manager


# Register your models here.

# admin.site.register(Fitness_Level)
# admin.site.register(Airman)
# admin.site.register(Physical_Training_Leader)
# admin.site.register(Profile)
# admin.site.register(Failure)
# admin.site.register(Unit_Fitness_Program_Manager)

@admin.register(Fitness_Level)
class FitnessLevelAdmin(admin.ModelAdmin):
    pass


@admin.register(Airman)
class AirmanAdmin(admin.ModelAdmin):
    list_display = ('rank', 'first_name', 'middle_initial', 'last_name', 'test_date')
    list_filter = ('first_name', 'last_name', 'test_date')
    search_fields = ('first_name', 'last_name')
    prepopulated_fields = {'slug': ('ssn',)}
    date_hierarchy = 'test_date'
    ordering = ('test_date', 'last_name')

# @admin.register(Physical_Training_Leader)
# @admin.register(Profile)
# @admin.register(Failure)
# @admin.register(Unit_Fitness_Program_Manager)
