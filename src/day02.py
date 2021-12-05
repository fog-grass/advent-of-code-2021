from pathlib import Path

path = Path(__file__).parent / "../input/day02.txt"
with path.open() as file:
	data = file.read()
data = data.splitlines()
hor_count = 0
ver_count = 0
for item in data:
	if "down" in item:
		ver_count += int(item.split()[1])
		#print(f"{item}: {ver_count} (down)")
	elif "up" in item:
		ver_count -= int(item.split()[1])
		#print(f"{item}: {ver_count} (up)")
	else:
		hor_count += int(item.split()[1])
		#print(f"{item}: {hor_count} (forvard)")


print(hor_count * ver_count)

#~~~~#part2#~~~~#
hor_count = 0
ver_count = 0
aim = 0
for item in data:
	if "down" in item:
		aim += int(item.split()[1])
		#print(f"{item}: {aim} (increased)")
	elif "up" in item:
		aim -= int(item.split()[1])
		#print(f"{item}: {aim} (decreased)")
	else:
		hor_count += int(item.split()[1])
		ver_count += int(item.split()[1]) * aim
		#print(f"{item}: {hor_count} (forvard)")
		#print(f"{item}: {ver_count} (depth)")


print(hor_count * ver_count)
