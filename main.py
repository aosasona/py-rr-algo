import time
"""
An attempt to simulate the round-robin algorithm running a couple of processes
"""


def sim_round_robin(processes, clock_freq):
  cycles = 0
  remaining_processes = list(range(len(processes)))
  while True:
    if len(remaining_processes) == 0:
      print('All processes have now completed running! :)')
      break
    for idx, process in enumerate(processes):
      if remaining_processes.count(idx) == 0 or process['ctc'] == 0:
        continue
      print('[running]', process['name'])
      time.sleep(clock_freq / 100)  # pretending to do something
      process['ctc'] -= 1
      cycles += 1
      if process['ctc'] == 0:
        remaining_processes.remove(idx)
        print(f"--- {process['name']} completed ---")


# ctc = cycles to complete (representation the ideal number of cycles a process might need to complete its ops)
processes = [
  {
    'name': 'Process 1',
    'ctc': 22
  },
  {
    'name': 'Process 2',
    'ctc': 14
  },
  {
    'name': 'Process 3',
    'ctc': 75
  },
  {
    'name': 'Process 4',
    'ctc': 9
  },
]

# assuming our CPU switches context every 10ms
sim_round_robin(processes, 10)
