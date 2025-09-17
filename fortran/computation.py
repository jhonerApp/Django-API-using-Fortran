from . import Microchannels
from . import constants as matrix_const
import numpy

# from fortran_api.models import FortranResults

# global geometric parameters
battery_active_length = 2000.0
comsol_port_length = 0.635
port_width = 32.0
port_pitch = 11.52

# calculation parameters
channel_discretization_count = 120

# geometric channel C1
hydraulic_diameter_c1 = 1.81432360742706
cross_section_c1 = 3.35806857142857
aspect_ratio_c1 = 0.675555555555556
port_number_c1 = 7

# geometric channel C2
hydraulic_diameter_c2 = 1.96289044289044
cross_section_c2 = 4.10661333333333
aspect_ratio_c2 = 0.548736462093863
port_number_c2 = 3

# fuid steps C1
steps_count_c1 = 2
steps_c1 = []
tube_c1 = [66,34]
ingress_c1 = [1,0]
direction_c1 = [1,-1]
steps_c1.append([tube_c1[0], ingress_c1[0], direction_c1[0]])
steps_c1.append([tube_c1[1], ingress_c1[1], direction_c1[1]])

# fluid steps C2
step_count_c2 = 2
steps_c2 = []
tube_c2 = [50,50]
ingress_c2 = [1,0]
direction_c2 = [1,-1]
steps_c2.append([tube_c2[0], ingress_c2[0], direction_c2[0]])
steps_c2.append([tube_c2[1], ingress_c2[1], direction_c2[1]])

# input fluid condition C1
fluid_c1 = "R134a"
flow_rate_c1 = 1910.0
inlet_temperature_c1 = 75.0

# input fluid condition C2
fluid_c2 = "water"
flow_rate_c2 = 880.0
inlet_temperature_c2 = 15.0

# input fluid condition C3
fluid_c3 = "air"
inlet_temperature_c3 = 35.0
air_pressure = 0.101325
air_velocity = 2.30


def computefotranAutomatically():
    inputs = [
              battery_active_length,
              comsol_port_length,
              port_width,
              port_pitch,
              channel_discretization_count,
              hydraulic_diameter_c1,
              cross_section_c1,
              aspect_ratio_c1,
              port_number_c1,
              inlet_temperature_c1,
              flow_rate_c1,
              hydraulic_diameter_c2,
              cross_section_c2,
              aspect_ratio_c2,
              port_number_c2,
              inlet_temperature_c2,
              flow_rate_c2,
              inlet_temperature_c3,
              air_pressure,
              air_velocity
              ]

    # chiamata fortran
    result = Microchannels.double_flow(
             inputs,
             steps_c1,
             steps_c2,
             matrix_const.C1_SUBCOOLED_LIQUID,
             matrix_const.C1_TWO_PHASE,
             matrix_const.C1_SUPERHEATED_VAPOR,
             matrix_const.C1_DATA,
             matrix_const.C2_SUBCOOLED_LIQUID,
             matrix_const.C2_TWO_PHASE,
             matrix_const.C2_SUPERHEATED_VAPOR,
             matrix_const.C2_DATA,
             matrix_const.C3_SINGLE_PHASE,
             matrix_const.MATRIX_W1_C1,
             matrix_const.MATRIX_W1_C2,
             matrix_const.MATRIX_W2,
             matrix_const.INPUT_OUTPUT_SCALING
             )

    return result

def computefotranManually(FortranResults):
    # data = {
    #   'battery_active_length': FortranResults.get('battery_active_length'),
    # }
    # return data
    inputs = [
              FortranResults.get('battery_active_length'),
              FortranResults.get('comsol_port_length'),
              FortranResults.get('port_width'),
              FortranResults.get('port_pitch'),
              FortranResults.get('channel_discretization_count'),
              FortranResults.get('hydraulic_diameter_c1'),
              FortranResults.get('cross_section_c1'),
              FortranResults.get('aspect_ratio_c1'),
              FortranResults.get('port_number_c1'),
              FortranResults.get('inlet_temperature_c1'),
              FortranResults.get('flow_rate_c1'),
              FortranResults.get('hydraulic_diameter_c2'),
              FortranResults.get('cross_section_c2'),
              FortranResults.get('aspect_ratio_c2'),
              FortranResults.get('port_number_c2'),
              FortranResults.get('inlet_temperature_c2'),
              FortranResults.get('flow_rate_c2'),
              FortranResults.get('inlet_temperature_c3'),
              FortranResults.get('air_pressure'),
              FortranResults.get('air_velocity'),
              ]

    # chiamata fortran
    result = Microchannels.double_flow(
             inputs,
             steps_c1,
             steps_c2,
             matrix_const.C1_SUBCOOLED_LIQUID,
             matrix_const.C1_TWO_PHASE,
             matrix_const.C1_SUPERHEATED_VAPOR,
             matrix_const.C1_DATA,
             matrix_const.C2_SUBCOOLED_LIQUID,
             matrix_const.C2_TWO_PHASE,
             matrix_const.C2_SUPERHEATED_VAPOR,
             matrix_const.C2_DATA,
             matrix_const.C3_SINGLE_PHASE,
             matrix_const.MATRIX_W1_C1,
             matrix_const.MATRIX_W1_C2,
             matrix_const.MATRIX_W2,
             matrix_const.INPUT_OUTPUT_SCALING
             )

    return result
