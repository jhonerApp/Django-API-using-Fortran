import os
# from clean_input import extract_array
from .clean_input import extract_array

MATRIX_W1_C1 = extract_array(os.path.join(os.path.dirname(__file__), 'csvs', 'matrix_w1_c1.csv'))

MATRIX_W1_C1 = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"matrix_w1_c1.csv"))
MATRIX_W1_C2 = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"matrix_w1_c2.csv"))
MATRIX_W2 = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"matrix_w2.csv"))
MATRIX_W2_C1 = MATRIX_W2[0]
MATRIX_W2_C2 = MATRIX_W2[1]
INPUT_OUTPUT_SCALING = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"input_output_scaling.csv"))

C1_SUBCOOLED_LIQUID = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"c1_subcooled_liquid.csv"))
C1_TWO_PHASE = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"c1_two_phase.csv"))
C1_SUPERHEATED_VAPOR = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"c1_superheated_vapor.csv"))
C1_DATA = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"c1_data.csv"))

C2_SUBCOOLED_LIQUID = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"c2_subcooled_liquid.csv"))
C2_TWO_PHASE = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"c2_two_phase.csv"))
C2_SUPERHEATED_VAPOR = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"c2_superheated_vapor.csv"))
C2_DATA = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"c2_data.csv"))

C3_SINGLE_PHASE = extract_array(os.path.join(os.path.dirname(__file__), 'csvs',"c3_single_phase.csv"))
