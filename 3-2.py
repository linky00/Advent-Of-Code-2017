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
	
trianglesToBeSortedWeirdly = []

for i in range(0, len(triangles), 3):
	trianglesToBeSortedWeirdly.append(triangles[i:i+3])
	
trianglesSortedWeirdly = []

for groupOfTriangles in trianglesToBeSortedWeirdly:
	for i in range(0,3):
		trianglesSortedWeirdly.append(list([groupOfTriangles[0][i], groupOfTriangles[1][i], groupOfTriangles[2][i]]))

goodTriangles = []

for triangle in trianglesSortedWeirdly:
	if triangle[0] + triangle [1] > triangle[2] and triangle[1] + triangle [2] > triangle[0] and triangle[2] + triangle [0] > triangle[1]:
		goodTriangles.append(list(triangle))
		
print(len(goodTriangles))