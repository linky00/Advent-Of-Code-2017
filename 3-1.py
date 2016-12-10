trianglesString = open('3-input.txt', 'r').read()
trianglesSplit = trianglesString.splitlines()
trianglesNotInt = []
for triangleToArray in trianglesSplit:
	trianglesNotInt.append(triangleToArray.split(' '))

triangles = []	

for triangle in trianglesNotInt:
	while '' in triangle:
		triangle.remove('')
	triangle = list(map(int, triangle))
	triangles.append(list(triangle))

goodTriangles = []

for triangle in triangles:
	if triangle[0] + triangle [1] > triangle[2] and triangle[1] + triangle [2] > triangle[0] and triangle[2] + triangle [0] > triangle[1]:
		goodTriangles.append(list(triangle))
		
print(len(goodTriangles))