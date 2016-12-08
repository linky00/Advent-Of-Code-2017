instructionsString = open('2-input.txt', 'r').read()
instructionsSplit = instructionsString.splitlines()

keypad = [
[' ', ' ', '1', ' ', ' '],
[' ', '2', '3', '4', ' '],
['5', '6', '7', '8', '9'],
[' ', 'A', 'B', 'C', ' '],
[' ', ' ', 'D', ' ', ' ']
]	

location = [1, 1]
finalOutput = ''

def GetNumber(inputLocation):
	return keypad[inputLocation[1]][inputLocation[0]]
	
for instructionLine in instructionsSplit:
	instructions = list(instructionLine)
	for instruction in instructions:
		if instruction == 'U' and GetNumber(list([location[0], location[1] - 1])) != ' ' and location[1] > 0:
			location[1] -= 1
		elif instruction == 'D' and GetNumber(list([location[0], location[1] + 1])) != ' ' and location[1] < 2:
			location[1] += 1
		elif instruction == 'L' and GetNumber(list([location[0] - 1, location[1]])) != ' ' and location[0] > 0:
			location[0] -= 1
		elif instruction == 'R' and GetNumber(list([location[0] + 1, location[1]])) != ' ' and location[0] < 2:
			location[0] += 1
		
	print(location)
	finalOutput = finalOutput + GetNumber(location)
	
print(finalOutput)