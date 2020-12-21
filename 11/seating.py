with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)
