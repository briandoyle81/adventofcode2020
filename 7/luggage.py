# should be using with...
with open('data.txt', 'r') as file:
    luggage_rules_data = file.read().split('\n')

# cut trailing newline
luggage_rules_data.pop(-1)


# need to parse the rules into a logical data structure

# all bags have adjective, then color

# Some cleanup needed

# rule format is bag, word "contains", either comma separated
# or "contain no other bags"

# dictionary with list of bags contained:

# or dict of dicts, because we have quantities

# sample = {
#     "light red": {
#         "bright white": 1,
#         "muted yellow": 2
#     }
# }

# do this then use to figure out permutations.  or is it combinations?

rules_dict = dict()

for rule in luggage_rules_data:
    new_rule = dict()
    rule = rule.strip('.')
    # breakpoint()
    split = rule.split(' contain ')
    outer_bag = split[0][:-5]

    contained_bags_string = split[1]

    if contained_bags_string != 'no other bags':
        contained_bags_list = contained_bags_string.split(', ')
        for contained in contained_bags_list:
            # only single digit numbers of bags so easy to parse
            # first digit is amount
            amount = int(contained[0])
            # account for bag or bags
            # No ternary in  python :(
            bag_length = None
            if contained[-1] == 's':
                bag_length = -5
            else:
                bag_length = -4
            name = contained[2:bag_length]
            new_rule[name] = amount

    rules_dict[outer_bag] = new_rule

print(rules_dict)

# Now to find how many colors can eventually carry a gold bag.

# Rules list for colors is also the list of colors, so iterate through that

# counter
# For each rule in rules_dict
# Continue if shiny gold, needs to be in a bag
# if rule contains shiny gold bag, + 1 and continue

# This should/could be recursive.  Or can use while rule not empty

# This might have infinite loops.  Continue when we get there
# could be a recursive base case
