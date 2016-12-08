import sys

instructionsString = 'L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2'
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