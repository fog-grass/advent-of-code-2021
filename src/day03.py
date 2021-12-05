from pathlib import Path

path = Path(__file__).parent / "../input/day03.txt"
with path.open() as file:
	data = file.read()
data = data.splitlines()
stats = {}
power_use = 0
gamma = ""
epsilon = ""
for j in range(len(data[0])):
	stats.update({j : [0, 0]})
for item in data:
	for i, j in enumerate(item):
		stats[i][int(j)] += 1
for item in stats:
	gamma += str(stats[item].index(max(stats[item])))
	epsilon += str(stats[item].index(min(stats[item])))
#print(stats)
#print(gamma)
#print(epsilon)
power_use = int(gamma, 2) * int(epsilon, 2)
print(power_use)

#~~~~#part2#~~~~#
with path.open() as file:
	data = file.read()
o2_rawlist = data.splitlines()
co2_rawlist = data.splitlines()
data = data.splitlines()
stats = {}
o2_list = []
co2_list = []
life_sup = 1
for i in range(len(data[0])):
	stats.update({i : [0, 0]})
	for item in o2_rawlist:		
		stats[i][int(item[i])] += 1
	for o2_record in o2_rawlist:
		if int(stats[i][0]) == int(stats[i][1]) and int(o2_record[i]) == 1:
			o2_list.append(o2_record)
			continue
		if int(o2_record[i]) == int(stats[i].index(max(stats[i]))):
			o2_list.append(o2_record)
	o2_rawlist = o2_list.copy()
	o2_list = []
	if len(o2_rawlist) == 2:
		life_sup *= max([int(o2_rawlist[0], 2), int(o2_rawlist[1], 2)])
		break
for i in range(len(data[0])):
	stats.update({i : [0, 0]})
	for item in co2_rawlist:
		stats[i][int(item[i])] += 1
	for co2_record in co2_rawlist:
		if int(stats[i][0]) == int(stats[i][1]) and int(co2_record[i]) == 0:
			co2_list.append(co2_record)
			continue
		if int(co2_record[i]) == int(stats[i].index(min(stats[i]))):
			co2_list.append(co2_record)
	co2_rawlist = co2_list.copy()
	co2_list = []
	if len(co2_rawlist) == 2:
		life_sup *= min([int(co2_rawlist[0], 2), int(co2_rawlist[1], 2)])
		break	
print(life_sup)


