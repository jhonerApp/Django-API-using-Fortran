"""
Fortran API models
"""
from django.db import models
# Create your models here.

class FortranResults(models.Model):
    battery_active_length = models.FloatField()
    comsol_port_length = models.FloatField()
    port_width  = models.FloatField()
    port_pitch = models.FloatField()
    channel_discretization_count = models.IntegerField()
    hydraulic_diameter_c1 = models.FloatField()
    cross_section_c1 = models.FloatField()
    aspect_ratio_c1 = models.FloatField()
    port_number_c1 = models.IntegerField()
    inlet_temperature_c1 = models.FloatField()
    flow_rate_c1 = models.FloatField()
    hydraulic_diameter_c2 = models.FloatField()
    cross_section_c2 = models.FloatField()
    aspect_ratio_c2 = models.FloatField()
    port_number_c2 = models.IntegerField()
    inlet_temperature_c2 = models.FloatField()
    flow_rate_c2 = models.FloatField()
    inlet_temperature_c3 = models.FloatField()
    air_pressure = models.FloatField()
    air_velocity = models.FloatField()



    # steps_count_c1 = models.IntegerField()
    # tube_c1 = models.JSONField(default=list)
    # steps_c1 = models.JSONField(default=list)
    # ingress_c1  = models.JSONField(default=list)
    # direction_c1 = models.JSONField(default=list)
    # step_count_c2 = models.IntegerField()
    # steps_c2 = models.JSONField(default=list)
    # tube_c2 = models.JSONField(default=list)
    # ingress_c2 = models.JSONField(default=list)
    # direction_c2 = models.JSONField(default=list)
    # fluid_c1 = models.CharField(max_length=100)
    # fluid_c2 = models.CharField(max_length=100)
    # fluid_c3 =  models.CharField(max_length=100)


