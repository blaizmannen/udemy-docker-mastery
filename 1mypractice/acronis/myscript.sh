#! /bin/bash

shopt -s extglob

declare -A sc # stat current

while true; do
  # Collect stats and calculate delta.
  declare -A sd=() # stat difference
  for s in /proc/+([0-9])/stat; do
    read p u < <(cut -d ' ' -f 1,14 "$s")
    sd[$p]=$(($u - ${sc[$p]-0}))
    sc[$p]=$u
  done
  # Remove terminted pids.
  for p in "${!sd[@]}"; do
    if [[ ! -v "sc[$p]" ]]; then
      unset "sc[$p]"
    fi
  done
  # Print top three.
  if [[ ${first:-yes} == yes ]]; then
    first=no
    printf "Collecting data...\n"
  else
    clear
    for p in "${!sd[@]}"; do
      printf "%d %d\n" "$p" "${sd[$p]}"
    done |
      sort -r -n -k2 |
      head -n3 |
      while read p d; do
        printf "%6d %4d %s\n" "$p" "$d" "$(readlink /proc/$p/exe)"
      done
  fi
  # Wait
  sleep 10
done


# Problem 1:
# The %CPU column is "CPU time used divided by the time the process has been running (cputime/realtime ratio), 
# expressed as a percentage.". 
# It is not "last 10 seconds", it is for the lifetime of the process thus far.

# To find out the % CPU time in the last 10 seconds,
# (cputime2 - cputime1) / (realtime2 - realtime1)
# This is more feasible as you only record the total process time and CPU time every 10 seconds
# and you use the differences to get the accurate calculations 

# Usage: in your working directory, save this file as myscript.sh
# and then from the working directory, execute the script with the command:  ~/myscript.sh