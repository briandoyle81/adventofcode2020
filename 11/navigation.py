with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

facing = 'E'

# half tempted to make a vector class
# x = 0
# y = 0

# fully tempted

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

position = Vector(0, 0)

def convert_to_cardinal(facing, char):
    # no need for something clever here
    # don't see this getting extended to more options
    if char == 'F':
        return facing

    # Reading the spec helps.  Right 90 is 90 degrees right
    # Not turn right and move 90!!!

    # if char == 'R':
    #     if facing == 'N':
    #         return 'E'
    #     if facing == 'S':
    #         return 'W'
    #     if facing == 'E':
    #         return 'S'
    #     if facing == 'W':
    #         return 'N'

    # if char == 'L':
    #     if facing == 'N':
    #         return 'W'
    #     if facing == 'S':
    #         return 'E'
    #     if facing == 'E':
    #         return 'N'
    #     if facing == 'W':
    #         return 'S'

    return char

def rotate_ship(facing, char, amount):
    # do need slightly fancy here, to handle any degrees
    rotation = {
                'N': ('W', 'E'),
                'E': ('N', 'S'),
                'S': ('E', 'W'),
                'W': ('S', 'N')
    }
    times = amount // 90

    if char == 'L':
        turn_index = 0
    if char == 'R':
        turn_index = 1

    for _ in range(times):
        facing = rotation[facing][turn_index]

    return facing


for instruction in data:
    char = convert_to_cardinal(facing, instruction[0])
    amount = int(instruction[1:])

    # state machine for this one, easy peasy

    # actually, convert relative to cardinal

    # cardinal directions are simple, so those first
    # North and east are positive.
    if char == 'N':
        position.y += amount
    elif char == 'S':
        position.y -= amount
    elif char == 'E':
        position.x += amount
    elif char == 'W':
        position.x -= amount
    else:
        # rotate the ship
        facing = rotate_ship(facing, char, amount)



    # print(f'{position.x}, {position.y}')

print(abs(position.x) + abs(position.y))
