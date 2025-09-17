## this is a GNU Octave scipt
## author: Nicola Suzzi
## email: nicola.suzzi@uniud.it, nicola.suzzi@libero.it
pkg load io
fli = ['TK_DF_RW.ods'];
## FLUID C1 ####################################################################
numarr = xlsread(fli, 'C1_prop','C14:I63');
flo = ['c1_subcooled_liquid.csv'];
fid = fopen(flo,'w');
fprintf(fid,'"%E","%E","%E","%E","%E","%E","%E"\n',numarr')
fclose(fid);
##
numarr = xlsread(fli, 'C1_prop','R14:X63');
flo = ['c1_superheated_vapor.csv'];
fid = fopen(flo,'w');
fprintf(fid,'"%E","%E","%E","%E","%E","%E","%E"\n',numarr')
fclose(fid);
##
numarr = xlsread(fli, 'C1_prop','L14:O63');
flo = ['c1_two_phase.csv'];
fid = fopen(flo,'w');
fprintf(fid,'"%E","%E","%E","%E"\n',numarr')
fclose(fid);
##
numarr = xlsread(fli, 'C1_prop','K4:L5');
h_C1_liq_sat = numarr(1,1);
T_C1_liq_sat = numarr(1,2);
h_C1_vap_sat = numarr(2,1);
T_C1_vap_sat = numarr(2,2);
numarr = xlsread(fli, 'C1_prop','E3:F7');
p_C1 = numarr(2,1);
p_C1_cr = numarr(5,1);
flo = ['c1_data.csv'];
fid = fopen(flo,'w');
fprintf( fid, '"%E"\n', p_C1 )
fprintf( fid, '"%E"\n', h_C1_liq_sat )
fprintf( fid, '"%E"\n', h_C1_vap_sat )
fprintf( fid, '"%E"\n', T_C1_vap_sat )
fprintf( fid, '"%E"\n', T_C1_liq_sat )
fprintf( fid, '"%E"\n', p_C1_cr )
fclose(fid);
## FLUID C2 ####################################################################
numarr = xlsread(fli, 'C2_prop','C14:I63');
flo = ['c2_subcooled_liquid.csv'];
fid = fopen(flo,'w');
fprintf(fid,'"%E","%E","%E","%E","%E","%E","%E"\n',numarr')
fclose(fid);
##
numarr = xlsread(fli, 'C2_prop','R14:X63');
flo = ['c2_superheated_vapor.csv'];
fid = fopen(flo,'w');
fprintf(fid,'"%E","%E","%E","%E","%E","%E","%E"\n',numarr')
fclose(fid);
##
numarr = xlsread(fli, 'C2_prop','L14:O63');
flo = ['c2_two_phase.csv'];
fid = fopen(flo,'w');
fprintf(fid,'"%E","%E","%E","%E"\n',numarr')
fclose(fid);
##
numarr = xlsread(fli, 'C2_prop','K4:L5');
h_C2_liq_sat = numarr(1,1);
T_C2_liq_sat = numarr(1,2);
h_C2_vap_sat = numarr(2,1);
T_C2_vap_sat = numarr(2,2);
numarr = xlsread(fli, 'C2_prop','E3:F7');
p_C2 = numarr(2,1);
p_C2_cr = numarr(5,1);
flo = ['c2_data.csv'];
fid = fopen(flo,'w');
fprintf( fid, '"%E"\n', p_C2 )
fprintf( fid, '"%E"\n', h_C2_liq_sat )
fprintf( fid, '"%E"\n', h_C2_vap_sat )
fprintf( fid, '"%E"\n', T_C2_vap_sat )
fprintf( fid, '"%E"\n', T_C2_liq_sat )
fprintf( fid, '"%E"\n', p_C2_cr )
fclose(fid);
## FLUID C3 ####################################################################
numarr = xlsread(fli, 'C3_prop','C14:I63');
flo = ['c3_single_phase.csv'];
fid = fopen(flo,'w');
fprintf(fid,'"%E","%E","%E","%E","%E","%E","%E"\n',numarr')
fclose(fid);
## NEURAL NETWORK MATRICES #####################################################
numarr = xlsread(fli, 'NN_RW', 'G4:M18');
flo = 'matrix_w1_c1.csv';
fid = fopen(flo,'w');
fprintf(fid,'"%E","%E","%E","%E","%E","%E","%E"\n',numarr')
fclose(fid);
flo = 'matrix_w1_c2.csv';
fid = fopen(flo,'w');
fprintf(fid,'"%E","%E","%E","%E","%E","%E","%E"\n',numarr')
fclose(fid);
numarr = xlsread(fli, 'NN_RW', 'G23:V24');
flo = 'matrix_w2.csv';
fmt = '';
for i = 1:15
  fmt = [fmt,'"%E",'];
endfor
fmt = [fmt,'"%E"\n'];
fid = fopen(flo,'w');
fprintf(fid, [fmt], numarr')
fclose(fid);
numarr = xlsread(fli, 'NN_RW', 'D4:E11');
flo = 'input_output_scaling.csv';
fid = fopen(flo,'w');
fprintf(fid,'"%E","%E"\n', numarr')
fclose(fid);



