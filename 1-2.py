import sys

instructionsString = open('1-input.txt', 'r').read()
instructions = instructionsString.split(', ')
direction = 0
location = [0, 0]
visitedLocations = []	

def AddToVisited():
	visitedLocations.append(list(location))


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
	
	while moveBy != 0:
		if direction == 0:
			location[1] += 1
			AddToVisited()
		elif direction == 1:
			location[0] += 1
			AddToVisited()
		elif direction == 2:
			location[1] -= 1
			AddToVisited()
		elif direction == 3:
			location[0] -= 1
			AddToVisited()
		moveBy -= 1

testableLocations = []
for visitedLocation in visitedLocations:
	for testLocation in testableLocations:
		if visitedLocation == testLocation:
			distance = abs(visitedLocation[0]) + abs(visitedLocation[1])
			print(distance)
			sys.exit()
	testableLocations.append(list(visitedLocation))