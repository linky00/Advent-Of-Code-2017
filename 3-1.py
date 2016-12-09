trianglesString = open('3-input.txt', 'r').read()
trianglesSplit = trianglesString.splitlines()
triangles = []
for triangleToArray in trianglesSplit:
	triangles.append(triangleToArray.split(' '))

for triangle in triangles:
	while '' in triangle:
		triangle.remove('')
	triangle = list(map(int, triangle))

goodTriangles = []

for triangle in triangles:
	if triangle[0] + triangle [1] > triangle[2] and triangle[1] + triangle [2] > triangle[0] and triangle[2] + triangle [0] > triangle[1]:
		goodTriangles.append(list(triangle))
		
print(len(goodTriangles))