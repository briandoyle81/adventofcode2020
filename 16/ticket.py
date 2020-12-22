with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

for i in range(len(data)):
    if data[i] == 'nearby tickets:':
        ticket_index = i + 1

# 25 + are tickets
tickets = data[ticket_index:]
# breakpoint()
# put rules in a dict
rule_dict = dict()

row = 0
while data[row] != "":
    split_rules = data[row].split(': ')
    rule_name = split_rules[0]
    ranges = split_rules[1].split(' or ')
    range0 = ranges[0].split('-')
    range1 = ranges[1].split('-')

    # use nested tuple for rules
    # ((min, max), (min, max))
    rule_dict[rule_name] = ((int(range0[0]), int(range0[1])), (int(range1[0]), int(range1[1])))

    row += 1

# print(rule_dict)

# now need to find all invalid values for any field and add them up

# like frequency queries?  Except not continuous masking
# build a mask?
# small ruleset
# use a set as a mask, 0(1) lookup for validity

filter_set = set()

for rule_name, rule_ranges in rule_dict.items():
    for rng in rule_ranges:
        for i in range(rng[0], rng[1] + 1):
            filter_set.add(i)

# print(filter_set)

# find invalid

invalid = []

for ticket in tickets:
    # get the numbers
    numbers = ticket.split(',')
    numbers = [int(num) for num in numbers]

    for number in numbers:
        if number not in filter_set:
            invalid.append(number)

print(sum(invalid))
