from pathlib import Path

path = Path(__file__).parent / "../input/day05.txt"
with path.open() as file:
	data = file.read()
data =  data.splitlines()
for i, line in enumerate(data):
	data[i] = [[int(cord) for cord in point.split(",")] for point in line.split(" -> ")]
#print(data)
dniwe = []
counter = 0
for a in range(999):
	dniwe.append([])
	for b in range(999):
		dniwe[a].append(0)
for line in data:
	if line[0][0] == line[1][0]:
		for i in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
			dniwe[i][line[0][0]] += 1
			if dniwe[i][line[0][0]] == 2:
				counter += 1
	elif line[0][1] == line[1][1]:
		for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
			dniwe[line[0][1]][i] += 1
			if dniwe[line[0][1]][i] == 2:
				counter += 1
#~~COMMENT BLOCK FOR PART 1~~#part 2#~~COMMENT BLOCK FOR PART 1~~#
	elif line[0][0] - line[1][0] == line[0][1] - line[1][1]:
		#print(line)
		j = min(line[0][1], line[1][1])
		for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
			dniwe[j][i] += 1
			#print(f"45 point [{i}, {j}]")
			if dniwe[j][i] == 2:
				counter += 1
			j += 1
	elif abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1]):
		#print(line)
		j = max(line[0][1], line[1][1])
		for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
			dniwe[j][i] += 1
			#print(f"-45 point [{i}, {j}]")
			if dniwe[j][i] == 2:
				counter += 1
			j -= 1
#~~~~#part 2 end#~~~~#
print(counter)
"""for i in dniwe:
	print(i)"""
#print(dniwe)
