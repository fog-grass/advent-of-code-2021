from pathlib import Path

path = Path(__file__).parent / "../input/day09.txt"
with path.open() as file:
	data = file.read()
data = [str(d_line) for d_line in data.splitlines()]
#print(data)
def get_basin(y, x, loc_bas):
	point_coord = str(y)+"|"+str(x)
	loc_bas.add(point_coord)
	left = [9, 0, 0]
	right = [9, 0, 0]
	up = [9, 0, 0]
	down = [9, 0, 0]		
	if x > 0:
		left = [int(data[y][x- 1]), y, x- 1]
	if x < len(data[y]) - 1:
		right = [int(data[y][x+ 1]), y, x+ 1]
	if y > 0:
		up = [int(data[y- 1][x]), y- 1, x]
	if y < len(data) - 1:
		down = [int(data[y+ 1][x]), y+ 1, x]
	neighbors = [left, right, up, down]
	for s in range(len(neighbors)):
		if neighbors[s][0] > int(data[y][x]) and neighbors[s][0] != 9:
			get_basin(neighbors[s][1], neighbors[s][2], loc_bas)
	return loc_bas


risk_count = 0
basin_set = []
for line in range(len(data)):
	for i in range(len(str(data[line]))):
		left = 9
		right = 9
		up = 9
		down = 9		
		if i > 0:
			left = int(data[line][i- 1])
		if i < len(data[line]) - 1:
			right = int(data[line][i+ 1])
		if line > 0:
			up = int(data[line- 1][i])
		if line < len(data) - 1:
			down = int(data[line+ 1][i])
		if min(up, down, left, right) > int(data[line][i]):
			loc_bas = set()
			risk_count += int(data[line][i]) + 1
			basin_set.append(get_basin(line, i, loc_bas))
print(risk_count)
print(basin_set)
part2 = 1
basin_len = []
for i in range(len(basin_set)):
	basin_len.append(len(basin_set[i]))
for j in range(3):
	part2 *= max(basin_len)
	#print(part2)
	print(max(basin_len))
	basin_len.remove(max(basin_len))
print(part2)

#data[line- 1][i], data[line+ 1][i], data[line][i- 1], data[line][i+ 1]