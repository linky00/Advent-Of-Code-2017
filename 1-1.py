instructionsString = open('1-input.txt', 'r').read()
instructions = instructionsString.split(', ')
direction = 0
location = [0, 0]

for instruction in instructions:
	if instruction[0] == 'L':
		direction -= 1
	elif instruction[0] == 'R':
		direction += 1
	
	if direction > 3:
		direction = 0
	elif direction < 0:
		direction = 3
	
	moveBy = int(instruction[1:])
	
	if direction == 0:
		location[1] += moveBy
	elif direction == 1:
		location[0] += moveBy
	elif direction == 2:
		location[1] -= moveBy
	elif direction == 3:
		location[0] -= moveBy

distance = abs(location[0]) + abs(location[1])
print(distance)
# IT WORKS!