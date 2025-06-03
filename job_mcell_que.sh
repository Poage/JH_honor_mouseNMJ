#!/bin/bash 

#SBATCH -J julisa-1h 
#SBATCH -N 1 
#SBATCH -p RM-shared 
#SBATCH -t 48:00:00 
#SBATCH --array=1-1000 
j=1000 

## run the job seed 1 to seed 4000
./mcell-binary-out -quiet -seed $((SLURM_ARRAY_TASK_ID)) -with_checks no AZmodel_mouse_main.mdl >> run.1.log 
./mcell-binary-out -quiet -seed $((SLURM_ARRAY_TASK_ID+$j)) -with_checks no AZmodel_mouse_main.mdl >> run.1.log 
./mcell-binary-out -quiet -seed $((SLURM_ARRAY_TASK_ID+$j*2)) -with_checks no AZmodel_mouse_main.mdl >> run.1.log 
./mcell-binary-out -quiet -seed $((SLURM_ARRAY_TASK_ID+$j*3)) -with_checks no AZmodel_mouse_main.mdl >> run.1.log 
./mcell-binary-out -quiet -seed $((SLURM_ARRAY_TASK_ID+$j*4)) -with_checks no AZmodel_mouse_main.mdl >> run.1.log 

