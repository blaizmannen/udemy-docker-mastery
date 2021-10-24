import psutil
import time

# no of processes to print the highest cpu usage
MAX_PROCESSES = 3

# complete duration of time to repeatedly retrieve CPU usage data
TIME_DURATION = 10

# time between retrieving cpu usage data from the system
TIME_STEP = 0.1

# column names defined in the psutils for getting process information
COL_PID = 'pid'
COL_NAME = 'name'
COL_CPU_PERCENTAGE = 'cpu_percent'

def getProcessorList():
  """
    Collect process id, name and CPU usage data in the current instant
  """
  procs = dict()

  # Iterate through all processes and collect the process information
  for procData in psutil.process_iter():
    # obtain the set of required attributes for the process
    procInfo = procData.as_dict(attrs=[COL_PID, COL_NAME, COL_CPU_PERCENTAGE])
    # save the information with process id as the key (we are assuming that the 
    # process id do not get reused within the time period)
    procs[procInfo[COL_PID]] = procInfo
  
  return procs

def collectCPUUsageData(timeDuration):
  """ 
    Collect CPU usage data for the given duration
  """
  timeElapsedData = list()
  # record the starting time
  start = time.time()
  # iterate and collect cpu usage data until given time duration has being elapsed
  while (time.time()-start) < timeDuration:
    # retrive the cpu usage data and save it to the list
    timeElapsedData.append(getProcessorList())
    # wait for a short period before next cpu usage data retrieval
    time.sleep(TIME_STEP)
  
  return timeElapsedData

def main():
  #---- Collect CPU Usage data for a given Duration ----#
  timeElapsedData = collectCPUUsageData(TIME_DURATION)

  #---- Group all CPU Usage data per process id ----#
  processCPUUsageValues = dict()
  processNames = dict()
  # iterate through all CPU usage records for each time step
  for allProcInfo in timeElapsedData:
    # iterate through all processes CPU usage data for the time step
    for pid in allProcInfo:
      # save the name of the process that the process id belongs to (will be used later)
      processNames[pid] = allProcInfo[pid][COL_NAME]

      # append the CPU usage of the process id 'pid' to the list that we collect CPU usage 
      # data of that 'pid'
      cpuData = processCPUUsageValues.setdefault(pid, list())     # get the list for the 'pid' usage data
      cpuData.append(allProcInfo[pid][COL_CPU_PERCENTAGE])        # append the new CPU usage data

  #---- Calculate the CPU Usage average for each Process Id ----#

  processCPUUAverages = list()

  # iterate through all processes containing CPU usage data list for each process id
  for pid in processCPUUsageValues:
    # calculate the average CPU usage for the process id 'pid
    avg = sum(processCPUUsageValues[pid])/len(processCPUUsageValues[pid])
    name = processNames[pid]
    # create a record containing process id, the name and the average CPU usage and add it
    # to a list for later sorting by average usage
    processCPUUAverages.append([pid, name, avg])

  # sort the list of by average usage in descending order
  processCPUUAverages.sort(key=lambda x: x[2], reverse=True)

  # pick only first MAX_PROCESSES since they would contain the heightest CPU usage average 
  # data
  highestProcesses = processCPUUAverages[:MAX_PROCESSES]

  #---- print the highest CPU usage data ----#

  # print a header
  # header = "%-15s%-20s%-10s" % ("Process ID", "Name", "CPU Usage")
  header = "{:15}{:20}{:>10}".format("Process ID", "Name", "CPU Usage")
  print(header)
  print('-' * len(header))
  for processData in highestProcesses:
    # print process data
    # print("%-15s%-20s%.2f%%" % (processData[0], processData[1], processData[2]))
    print("{:<15}{:<20}{:>8} %".format(processData[0], processData[1], round(processData[2],2)))

if __name__ == "__main__":
  main()