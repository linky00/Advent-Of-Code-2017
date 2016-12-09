trianglesString = open('3-input.txt', 'r').read()
trianglesSplit = trianglesString.splitlines()
triangles = []
for triangleToArray in trianglesSplit:
	triangles.append(triangleToArray.split(' '))

for triangle in triangles:
	for length in triangle:
		if length == '':
			del length
		length = int(length)

print(triangles)