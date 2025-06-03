# These codes are used to generate reaction parameter files for the multi-pulses az mcell simulation.
# the first parameter is the interval between pulses, the second on the number of
# pulses
# mkdir ./rate_constants
# cp ../xrate_constants/*template* rate_constants/
# python RATE_GEN.py 0.01 2 
# 0.01 is interstimulus interval 
# 2 is number of pulses



import sys
import os

interval=float((sys.argv)[1])
num_of_pulses=int((sys.argv)[2])

os.chdir("./rate_constants")

def Make_New_Parameter_File_1(template_name,interval):
    parameter_change_time_step=0.00002
    if interval<0.003:
        print ("Error: Interval cannot be shorter than 0.003s.\n")
        exit(0)
    f_in=open(template_name)
    output_name=template_name[0:len(template_name)-13]+".txt"
    f_out=open(output_name,'w')
    line=f_in.readline()
    token=line.split()
    first_value=float(token[1])
    f_out.write(line)
    while 1:
        line=f_in.readline()
        if not line: break
        f_out.write(line)
        line_backup=line
    token=line_backup.split()
    last_value=float(token[1])
    f_in.close()
    
    mid_interval_steps=int((interval-0.003)/parameter_change_time_step)
    
    for p in range(1,num_of_pulses):
        for i in range(1,mid_interval_steps):
            output_line=str(0.003+(p-1)*interval+i*parameter_change_time_step)+'  '+str(last_value-(last_value-first_value)/mid_interval_steps*i)+'\n'
            f_out.write(output_line)
    
        f_in=open(template_name)
        while 1:
            line=f_in.readline()
            if not line: break
            token=line.split()
            time=float(token[0])
            output_line=str(str(time+interval+(p-1)*interval))+'  '+token[1]+'\n'
            f_out.write(output_line)

    f_out.close()


def Make_New_Parameter_File_2(template_name,interval):
    parameter_change_time_step=0.00002
    if interval<0.003:
        print ("Error: Interval cannot be shorter than 0.003s.\n")
        exit(0)
    
    total_t=interval*(num_of_pulses-1)+0.003
    for p in range(1,num_of_pulses+1):
        f_in=open(template_name)
        output_name="k3_control_short_"+str(p)+".txt"
        f_out=open(output_name,'w')
        start_t=interval*(p-1)
        end_t=start_t+0.003
        t=0
        while t<=total_t:
            if t>=start_t and t<=end_t:
                line=f_in.readline()
                token=line.split()
                output_line=str(t)+"    "+token[1]+"\n"
            else:
                output_line=str(t)+"    "+'0\n'
            f_out.write(output_line)
            t=t+parameter_change_time_step

        f_in.close()
        f_out.close()


Make_New_Parameter_File_1('ac1c2_template.txt',interval)
Make_New_Parameter_File_1('bc2c1_template.txt',interval)
Make_New_Parameter_File_1('ac2c3_template.txt',interval)
Make_New_Parameter_File_1('bc3c2_template.txt',interval)
Make_New_Parameter_File_1('ac3o1_template.txt',interval)
Make_New_Parameter_File_1('bo1c3_template.txt',interval)
Make_New_Parameter_File_2('k3_control_short_template.txt',interval)

