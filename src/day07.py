from pathlib import Path
import math

path = Path(__file__).parent / "../input/day07.txt"
with path.open() as file:
	data = file.read()
data = sorted([int(crab) for crab in data.split(",")])
#print(data)
if len(data) % 2 == 0:
	allinged_position = (data[len(data)//2] + data[len(data)//2 - 1]) // 2
else:
	allinged_position = data[len(data)//2]
#print(allinged_position)
fuel = 0
for crab in data:
	fuel += abs(allinged_position - crab) 
print(fuel)
allinged_position = sum(data) / len(data)
if allinged_position - int(allinged_position) < 0.6:
	allinged_position = math.trunc(allinged_position)
else:
	allinged_position = round(allinged_position)
print(allinged_position)
fuel = 0
for crab in data:
	x = abs(allinged_position - crab)
	fuel += x*(x + 1)//2
print(fuel)