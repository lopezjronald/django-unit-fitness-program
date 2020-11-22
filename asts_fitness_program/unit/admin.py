from django.contrib import admin
from .models import Airman, Physical_Training_Leader, Profile, Failure, Unit_Fitness_Program_Manager


# Register your models here.
# admin.site.register(Airman)
@admin.register(Airman)
class AirmanAdmin(admin.ModelAdmin):
    list_display = ('rank', 'first_name', 'middle_initial', 'last_name', 'test_date')
    list_filter = ('first_name', 'last_name', 'test_date')
    search_fields = ('first_name', 'last_name')
    prepopulated_fields = {'airman_slug': ('ssn',)}
    date_hierarchy = 'test_date'
    ordering = ('test_date', 'last_name')


# @admin.register(Physical_Training_Leader)
@admin.register(Physical_Training_Leader)
class PhysicalTrainingLeader(admin.ModelAdmin):
    list_display = ('airman_id', 'ptl_certification_date', 'ptl_expiration_date', 'cpr_expiration_date')
    list_filter = ('ptl_expiration_date', 'cpr_expiration_date')
    date_hierarchy = 'ptl_expiration_date'
    ordering = ('-ptl_expiration_date', '-cpr_expiration_date')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('airman_id', 'profile_start_date', 'profile_expiration_date',)
    list_filter = ('profile_expiration_date',)
    date_hierarchy = 'profile_expiration_date'
    ordering = ('-profile_expiration_date',)


@admin.register(Failure)
class FailureAdmin(admin.ModelAdmin):
    list_display = ('airman_id', 'failure_date', 'be_well_completion_date',)
    list_filter = ('failure_date',)
    search_fields = ('failure_date',)
    date_hierarchy = 'failure_date'
    ordering = ('-failure_date',)


@admin.register(Unit_Fitness_Program_Manager)
class UnitFitnessProgramManagerAdmin(admin.ModelAdmin):
    list_display = ('airman_id', 'ufpm_expiration_date')
    list_filter = ('ufpm_expiration_date',)
    date_hierarchy = 'ufpm_expiration_date'
    ordering = ('-ufpm_expiration_date',)
