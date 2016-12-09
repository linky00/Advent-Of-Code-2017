instructionsString = open('2-input.txt', 'r').read()
instructionsSplit = instructionsString.splitlines()

keypad = [
[' ', ' ', '1', ' ', ' '],
[' ', '2', '3', '4', ' '],
['5', '6', '7', '8', '9'],
[' ', 'A', 'B', 'C', ' '],
[' ', ' ', 'D', ' ', ' ']
]	

location = [0,2]
finalOutput = ''

def GetNumber(inputLocation):
	try:
		return keypad[inputLocation[1]][inputLocation[0]]
	except IndexError:
		return None
	
for instructionLine in instructionsSplit:
	instructions = list(instructionLine)
	for instruction in instructions:
		if instruction == 'U' and GetNumber(list([location[0], location[1] - 1])) != ' ' and location[1] > 0:
			location[1] -= 1
		elif instruction == 'D' and GetNumber(list([location[0], location[1] + 1])) != ' ' and location[1] < 4:
			location[1] += 1
		elif instruction == 'L' and GetNumber(list([location[0] - 1, location[1]])) != ' ' and location[0] > 0:
			location[0] -= 1
		elif instruction == 'R' and GetNumber(list([location[0] + 1, location[1]])) != ' ' and location[0] < 4:
			location[0] += 1
					
	finalOutput = finalOutput + GetNumber(location)
	
print(finalOutput)