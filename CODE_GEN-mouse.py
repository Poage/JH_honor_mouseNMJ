# These scripts are used to generate codes in mdl for the multi-pulse model in frog az mcell simulations.
# Input pulse_num = number of pulses 

import sys

if len(sys.argv) == 1:
	pulse_num = 2
else:
	pulse_num = int((sys.argv)[1])



#################
# molecules.mdl #
#################


channel = ['1_1_1','1_1_2','1_1_3','1_1_4',\
'2_1_1','2_1_2','2_1_3','2_1_4',\
'3_1_1','3_1_2','3_1_3','3_1_4',\
'4_1_1','4_1_2','4_1_3','4_1_4',\
'5_1_1','5_1_2','5_1_3','5_1_4',\
'6_1_1','6_1_2','6_1_3','6_1_4'] 


f = open("molecules.mdl",'w')

out = "DEFINE_MOLECULES {\n\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "ca_" + i + "_" + str(pulse) + "{ DIFFUSION_CONSTANT_3D = ca_diff_const }\n"
		f.write(out)

out = "\n\n\n" + "unbound_sensor { DIFFUSION_CONSTANT_2D = 0 }\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "bound_sensor_" + i + "_" + str(pulse) + "{ DIFFUSION_CONSTANT_2D = 0 }\n"
		f.write(out)

out = "\n\n\n" + "unbound_sensor_Y { DIFFUSION_CONSTANT_2D = 0 }\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "bound_sensor_Y_" + i + "_" + str(pulse) + "{ DIFFUSION_CONSTANT_2D = 0 }\n"
		f.write(out)



out = "\n\n\n" + "unbound_fixed_buffer { DIFFUSION_CONSTANT_3D = 0 }\n"
f.write(out)

for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "bound_fixed_buffer_" + i + "_" + str(pulse) + "{ DIFFUSION_CONSTANT_3D = 0 }\n"
                f.write(out)

out = "\n\n\n" + "unbound_mobile_buffer { DIFFUSION_CONSTANT_3D = mobile_buffer_diff_const }\n"
f.write(out)


for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "bound_mobile_buffer_" + i + "_" + str(pulse) + "{ DIFFUSION_CONSTANT_3D = mobile_buffer_diff_const }\n"
                f.write(out)


out = "\n\n\n"
f.write(out)


for i in channel:
	out = "closed_channel_" + i + "{ DIFFUSION_CONSTANT_2D = 0 }\n"
	f.write(out)
	out = "closed2_channel_" + i + "{ DIFFUSION_CONSTANT_2D = 0 }\n"
	f.write(out)
	out = "closed3_channel_" + i + "{ DIFFUSION_CONSTANT_2D = 0 }\n"
	f.write(out)
	out = "open1_channel_" + i + "{ DIFFUSION_CONSTANT_2D = 0 }\n"
	f.write(out)
	out = "open2_channel_" + i + "{ DIFFUSION_CONSTANT_2D = 0 }\n\n"
	f.write(out)



out = "\n}\n"
f.write(out)


f.close()




#######################
# surface_classes.mdl #
#######################

f = open("surface_classes.mdl",'w')

out = "DEFINE_SURFACE_CLASSES {\n\n"
f.write(out)

out = "absorb_all_calcium_ions {\n\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "ABSORPTIVE = ca_" + i + "_" + str(pulse) + "\n"
		f.write(out)

out = "\n\n}\n\n"
f.write(out)

out = "transparent_to_all_diffusing_molecules {\n\n"
f.write(out)

for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "TRANSPARENT = ca_" + i + "_" + str(pulse) + "\n"
                f.write(out)

out = "\n\n\nTRANSPARENT = unbound_mobile_buffer\n"
f.write(out)

for i in channel:
        for pulse in range(1,pulse_num+1):
                out = "TRANSPARENT = bound_mobile_buffer_" + i + "_" + str(pulse) + "\n"
                f.write(out)

out = "\n\n}\n\n} /*end define surface classes*/\n"
f.write(out)

f.close()


##########################
# reactions_template.mdl #
##########################

f = open("reactions.mdl",'w')

out = "DEFINE_REACTIONS {\n\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "unbound_sensor'+ca_" + i + "_" + str(pulse) + "' -> bound_sensor_" + i + "_" + str(pulse) + "' [sensor_onrate]\n"
		f.write(out)

out = "\n\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "bound_sensor_" + i + "_" + str(pulse) + "' -> unbound_sensor'+ca_" + i + "_" + str(pulse) + "' [sensor_offrate]\n"
		f.write(out)

out = "\n\n"
f.write(out)


for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "unbound_sensor_Y'+ca_" + i + "_" + str(pulse) + "' -> bound_sensor_Y_" + i + "_" + str(pulse) + "' [sensor_Y_onrate]\n"
		f.write(out)

out = "\n\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "bound_sensor_Y_" + i + "_" + str(pulse) + "' -> unbound_sensor_Y'+ca_" + i + "_" + str(pulse) + "' [sensor_Y_offrate]\n"
		f.write(out)

out = "\n\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "unbound_mobile_buffer+ca_" + i + "_" + str(pulse) + " -> bound_mobile_buffer_" + i + "_" + str(pulse) + " [mobile_buffer_onrate]\n"
		f.write(out)

out = "\n\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "bound_mobile_buffer_" + i + "_" + str(pulse) + " -> unbound_mobile_buffer+ca_" + i + "_" + str(pulse) + " [mobile_buffer_offrate]\n"
		f.write(out)


out = "\n\n"
f.write(out)


for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "unbound_fixed_buffer+ca_" + i + "_" + str(pulse) + " -> bound_fixed_buffer_" + i + "_" + str(pulse) + " [mobile_buffer_onrate]\n"
		f.write(out)

out = "\n\n"
f.write(out)

for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "bound_fixed_buffer_" + i + "_" + str(pulse) + " -> unbound_fixed_buffer+ca_" + i + "_" + str(pulse) + " [mobile_buffer_offrate]\n"
		f.write(out)


out = "\n\n"
f.write(out)

for i in channel:
	out = "closed_channel_" + i + "'->closed2_channel_" + i + "' [\"./rate_constants/ac1c2.txt\"]\n"
	f.write(out)
	out = "closed2_channel_" + i + "'->closed_channel_" + i + "' [\"./rate_constants/bc2c1.txt\"]\n"
	f.write(out)
	out = "closed2_channel_" + i + "'->closed3_channel_" + i + "' [\"./rate_constants/ac2c3.txt\"]\n"
	f.write(out)
	out = "closed3_channel_" + i + "'->closed2_channel_" + i + "' [\"./rate_constants/bc3c2.txt\"]\n"
	f.write(out)
	out = "closed3_channel_" + i + "'->open1_channel_" + i + "' [\"./rate_constants/ac3o1.txt\"]\n"
	f.write(out)
	out = "open1_channel_" + i + "'->closed3_channel_" + i + "' [\"./rate_constants/bo1c3.txt\"]\n"
	f.write(out)
	out = "open1_channel_" + i + "'->open2_channel_" + i + "' [2.5]\n"
	f.write(out)
	out = "open2_channel_" + i + "'->open1_channel_" + i + "' [200]\n"
	f.write(out)



	for pulse in range(1,pulse_num+1):
		out = "open1_channel_" + i + "' -> open1_channel_" + i + "'+ca_" + i + "_" + str(pulse) + "' [\"./rate_constants/k3_control_short_" + str(pulse) + ".txt\"]\n"
		f.write(out)
		out = "open2_channel_" + i + "' -> open2_channel_" + i + "'+ca_" + i + "_" + str(pulse) + "' [\"./rate_constants/k3_control_short_" + str(pulse) + ".txt\"]\n"
		f.write(out)
	out = "\n\n"
	f.write(out)

out = "\n\n\n}\n"
f.write(out)

f.close()


#####################
# reaction_data.mdl #
#####################

f = open("reaction_data.mdl",'w')

out = "REACTION_DATA_OUTPUT {\n\n\nBINARY_OUTPUT = TRUE\nBINARY_OUTPUT_COMPRESSION_LEVEL = 9\nBINARY_OUTPUT_COMPRESSION_TYPE = BZIP2\nBINARY_OUTPUT_DIRECTORY = binary_out\nBINARY_OUTPUT_FILENAME = \"seed_count.00\" & seed & \".bin.bz2\"\n\n\nSTEP = reaction_output_time_step\n\n"
f.write(out)

#out = "{"
#f.write(out)
#for i in channel:
#	for pulse in range(1,pulse_num+1):
#		out = "COUNT[bound_mobile_buffer_" + i + "_" + str(pulse) + ",WORLD]"
#		if pulse == pulse_num and channel.index(i) == len(channel)-1:
#			out = out + "}=> reactdir & \"buffer_bound.\" & seed & \".dat\"\n\n\n"
#		else:
#			out = out + "+\n"
#		f.write(out)

out = "{"
f.write(out)
for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "COUNT[bound_fixed_buffer_" + i + "_" + str(pulse) + ",WORLD]"
		if pulse == pulse_num and channel.index(i) == len(channel)-1:
			out = out + "}=> reactdir & \"buffer_bound.\" & seed & \".dat\"\n\n\n"
		else:
			out = out + "+\n"
		f.write(out)


for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "{COUNT[ca_" + i + "_" + str(pulse) + ",WORLD]}=> reactdir & \"ca_ions_" + i + "_" + str(pulse) + "\" & \".\" & seed & \".dat\"\n"
		f.write(out)

out = "\n\n\n{"
f.write(out)
for i in channel:
	for pulse in range(1,pulse_num+1):
		out = "COUNT[ca_" + i + "_" + str(pulse) + ",WORLD]"
		if pulse == pulse_num and channel.index(i) == len(channel)-1:
			out = out + "}=> reactdir & \"summed_ca_ions\" & \".\" & seed & \".dat\"\n\n\n"			
		else:
			out = out + "+\n"
		f.write(out)
	

for pulse in range(1,pulse_num+1):
	out = "{"
	f.write(out)
	for i in channel:
		out = "COUNT[ca_" + i + "_" + str(pulse) + ",WORLD]"
		if channel.index(i) == len(channel)-1:
			out = out + "}=> reactdir & \"summed_ca_ions_" + str(pulse) + "\" & \".\" & seed & \".dat\"\n\n\n"
		else:
			out = out + "+\n"
		f.write(out)

vesicle = ['1_1','1_2','2_1','2_2','3_1','3_2','4_1','4_2','5_1','5_2','6_1','6_2']

for v in vesicle:
        for j in channel:
                for pulse in range(1,pulse_num+1):
                         out = "{COUNT[bound_sensor_" + j + "_" + str(pulse) + ",presynaptic_segment.vesicles.sensor_" + v + "[sites_all]]} => reactdir & \"vesicle_" + v + "_ca_" + j + "_" + str(pulse) + ".\" & seed & \".dat\"\n"

                         f.write(out)

out = "\n\n"
f.write(out)

for v in vesicle:
        for j in channel:
                for pulse in range(1,pulse_num+1):
                        out = "{COUNT[bound_sensor_Y_" + j + "_" + str(pulse) + ",presynaptic_segment.vesicles.sensor_Y_" + v + "[sites_all]]} => reactdir & \"vesicle_Y_" + v + "_ca_" + j + "_" + str(pulse) + ".\" & seed & \".dat\"\n"
                        f.write(out)

out = "\n\n"
f.write(out)

########

for i in channel:
	out = "{COUNT[open1_channel_" + i + ",WORLD]+COUNT[open2_channel_" + i + ",WORLD]}=> reactdir & \"open_channel_" + i + "\" & \".\" & seed & \".dat\"\n"
	f.write(out)


out = "\n\n\n{"
f.write(out)

for i in channel:
	out = "COUNT[open1_channel_" + i + ",WORLD]+COUNT[open2_channel_" + i + ",WORLD]"
	if channel.index(i) == len(channel)-1:
		out = out + "}=> reactdir & \"summed_open_channels\" & \".\" & seed & \".dat\"\n\n\n"
	else:
		out = out + "+\n"
	f.write(out)


##X_sensor=[9,8,31,29,30,7,34,35,32,33,3,6,36,37,38,17,39,40,41,42,15,16,45,43,44,14,48,49,46,47,4,12,50,24,51,10,25,26,27,28]
##X_sensor.sort()
for X_sensor in range (0,52) :
	#if X_sensor<10 :
	#	i_tag='0'+str(X_sensor)
	#else:
	i_tag=str(X_sensor)
	for v in vesicle :
		v_tag = str(v)
		for l in range(1,pulse+1):
			for k in channel:
				base_out="COUNT[bound_sensor_"+str(k)+"_"+str(l)+",presynaptic_segment.vesicles.sensor_"+v_tag+"[site_"+i_tag+"]]"
				if len(channel)-1 == 0:
					out="{"+base_out+"}=>reactdir & \"bound_vesicle_"+v_tag+"_sensor_"+i_tag+"_"+str(l)+".\" & seed & \".dat\"\n\n"
		
				elif channel.index(k)==0 and len(channel)-1 != 0:
					out="{"+base_out+"+\n"
				elif channel.index(k)==len(channel)-1 and len(channel)-1 != 0:
					out=base_out+"}=>reactdir & \"bound_vesicle_"+v_tag+"_sensor_"+i_tag+"_"+str(l)+".\" & seed & \".dat\"\n\n"
				else:
					out=base_out+"+\n"
				f.write(out)	


out = "\n\n\n\n"
f.write(out)

for i in range (0,36):
	i_tag=str(i)
	for v in vesicle:
		v_tag=str(v)
		for l in range(1,pulse+1):
			for k in channel:
				base_out="COUNT[bound_sensor_Y"+"_"+k+"_"+str(l)+",presynaptic_segment.vesicles.sensor_Y_"+v_tag+"[site_"+str(i)+"]]"
				if len(channel)-1 == 0:
					out="{"+base_out+"}=>reactdir & \"bound_vesicle_"+v_tag+"_sensor_Y_"+i_tag+"_"+str(l)+".\" & seed & \".dat\"\n\n"
				elif channel.index(k)==0 and len(channel)-1 != 0:
					out="{"+base_out+"+\n"
				elif channel.index(k)==len(channel)-1 and len(channel)-1 != 0:
					out=base_out+"}=>reactdir & \"bound_vesicle_"+v_tag+"_sensor_Y_"+i_tag+"_"+str(l)+".\" & seed & \".dat\"\n\n"
				else:
					out=base_out+"+\n"
				f.write(out)

out = "\n}\n"

f.write(out)

f.close()










