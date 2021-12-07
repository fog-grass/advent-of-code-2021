from pathlib import Path

path = Path(__file__).parent / "../input/day06.txt"
with path.open() as file:
	data = file.read()
data = [int(fish) for fish in data.split(",")]
fish_packed = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
for fish in data:
	fish_packed[0][fish] += 1
#print(fish_packed)
day_count = 256
for day in range(day_count + 1):
	next_day = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	for fish in range(9):
		if fish == 8:
			next_day[fish] += fish_packed[day][0]
		elif fish == 6:
			next_day[fish] += fish_packed[day][0]
			next_day[fish] += fish_packed[day][fish + 1]
		else:
			next_day[fish] += fish_packed[day][fish + 1]
	fish_packed.append(next_day)
	if day == 80:
		print(f"After day {day}: {sum(fish_packed[day])}")
	#print(f"After day {day}: {fish_packed[day]}")
	#print(f"After day {day}: {sum(fish_packed[day])}")
print(f"After day {day_count}: {sum(fish_packed[day_count])}")