# M01T06: Triathlon Award Program
# This program calculates total triathlon time and determines the award based on completion time

# Get the time for each triathlon event (in minutes)
swimming_time = int(input("Enter the swimming time (in minutes): "))
cycling_time = int(input("Enter the cycling time (in minutes): "))
running_time = int(input("Enter the running time (in minutes): "))

# Calculate the total time
total_time = swimming_time + cycling_time + running_time

# Display the total time
print(f"Total time taken for the triathlon: {total_time} minutes")

# Determine the award based on total time
if total_time <= 100:
    print("Award: Provincial colours")
elif total_time <= 105:
    print("Award: Provincial half colours")
elif total_time <= 110:
    print("Award: Provincial scroll")
else:
    print("Award: No award")
