from pathlib import Path

path = Path(__file__).parent / "../input/day01.txt"
with path.open() as file:
	data = file.read()
data = [int(item) for item in data.splitlines()]
count = 0
for i in range(len(data)):
	if i == 0:
		print(f"{data[i]} (N/A - no previous measurement)")
	else:
		if int(data[i]) > int(data[i-1]):
			count += 1
			#print(f"{data[i]} (increased)")
		#else:
			#print(f"{data[i]} (decreased)")
print(count)

#~~~~~~~#part 2#~~~~~~#
count2 = 0
for j in range(len(data) - 2):
	if j == 0:
		print(f"{data[j] + data[j+1] + data[j+2]} (N/A - no previous measurement)")
	else: 
		if data[j] + data[j+1] + data[j+2] > data[j-1] + data[j] + data[j+1]:
			count2 += 1
			#print(f"{data[j] + data[j+1] + data[j+2]} (increased)")
		#elif data[j] + data[j+1] + data[j+2] < data[j-1] + data[j] + data[j+1]:
			#print(f"{data[j] + data[j+1] + data[j+2]} (decreased)")
		#else:
			#print(f"{data[j] + data[j+1] + data[j+2]} (no change)")
print(count2)