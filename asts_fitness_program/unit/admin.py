from django.contrib import admin
from .models import fitness_level, airmen, physical_training_leader, profile, failure, unit_fitness_program_manager

# Register your models here.
admin.site.register(fitness_level)
admin.site.register(airmen)
admin.site.register(physical_training_leader)
admin.site.register(profile)
admin.site.register(failure)
admin.site.register(unit_fitness_program_manager)