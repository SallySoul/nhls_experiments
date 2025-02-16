#!/bin/bash
#SBATCH --job-name=heat_2d_threads
#SBATCH --partition=compute
#SBATCH --account=sun127
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
#SBATCH --mem=120GB
#SBATCH --time=02:30:00
echo "JOB: Starting"

echo "JOB: Loading Modules"
module load gcc/10.2.0/npcyll4
module load python/3.8.12/7zdjza7

echo "JOB: Changing work dir"
cd /home/rbentley/nhls_experiments

echo "JOB: python version"
python --version

echo "JOB: running script"
python src/run_heat_2d_threads.py
