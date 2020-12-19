import math

with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# new data format!

earliest_departure = int(data[0])

# discard x's for now, probably part 2

def filter_x(value):
    if value == 'x':
        return False
    return True

busses = data[1].split(',')
busses = filter(filter_x, busses)

busses = [int(num) for num in busses]

print(busses)


# all busses started at time 0
# ID number is roundtrip time, the go constantly
# Dataset is small, brute forcing it

departure_times = []
closest_time = float('inf')
closest_bus = None
for i in range(0, len(busses)):
    time = 0
    while time < earliest_departure:
        time += busses[i]

    departure_times.append(time)
    if closest_time > time:
        closest_time = time
        closest_bus = busses[i]

print(closest_bus * (closest_time - earliest_departure))
