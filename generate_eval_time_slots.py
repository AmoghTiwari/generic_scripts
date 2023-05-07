from math import ceil, floor

""" Constraints """
max_time_hrs = None # In hours (set to None if specifiying time in minutes)
max_time_mins = None # In minutes (set to None if specifiying time in hours)
max_people_to_process = 36 # Set to None if no such limit

start_time = 2000
unit_time_mins = 5 # Unit time in minutes
buffer_after = None # Add buffer time after these many time units have elapsed
repeat_slot_start_times = True
repeat_slot_start_times_count = 2
display_end_time = False

if max_time_mins == None:
    if max_time_hrs != None:
        max_time_mins = int(max_time_hrs * 60)
    else:
        max_time_mins = float('inf')

if max_people_to_process == None:
    max_people_to_process = float('inf')

if max_time_mins == float('inf') and max_people_to_process == float('inf'):
    print("##### Erorr Message #####")
    print("'max_time_mins', 'max_time_hrs' and 'max_people_to_process', all 3 parameters are set to be None i.e., no constraint has been specified, either based on time, or based on max_people_to_process")
    print("Please specify at least one constraint. I am sure you do not want to do this work for the rest of your life :)")
    print("Exitting !!!")
    exit()

if max_time_mins != float('inf'):
    max_time_units = floor(max_time_mins / unit_time_mins)
else:
    max_time_units = float('inf')

if repeat_slot_start_times:
    if not isinstance(repeat_slot_start_times_count, int):
        print("'repeat_slot_start_times' is set to true. But repeat_slot_start_times_count is not an int")
        print("Can't work with this config")
        print("Exitting !!!")
    else:
        unit_time_mins = unit_time_mins * repeat_slot_start_times_count
        max_people_to_process = ceil(max_people_to_process/repeat_slot_start_times_count)

time_units_elapsed = 0; people_processed = 0; buffer_monitor = 0
printing_monitor = 0
while time_units_elapsed < max_time_units and people_processed < max_people_to_process:
    time_units_elapsed+= 1
    end_time = start_time + unit_time_mins
    if end_time % 100 == 60:
        end_time = 100*(end_time // 100 + 1)
    
    if buffer_after != None and time_units_elapsed % buffer_after == 0:
        time_units_elapsed+= 1
        start_time = end_time
        continue
    for i in range(repeat_slot_start_times_count):
        if display_end_time:
            print(f"{start_time} - {end_time}")
        else:
            print(f"{start_time}")
    time_units_elapsed+= 1
    people_processed+= 1
    start_time = end_time


if people_processed < max_people_to_process:
    print("Exitted due to time constraints")
elif time_units_elapsed < max_time_units:
    print("Exitted because the max number of people to process has been reached")

print(f"Total people processed = {people_processed}")
print(f"Total time used = {time_units_elapsed*unit_time_mins} minutes")
