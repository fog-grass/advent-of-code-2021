from pathlib import Path

path = Path(__file__).parent / "../input/day10.txt"
with path.open() as file:
	data = file.read()
data = data.splitlines()
#print(data)
matcher = {'(':')','[':']','{':'}','<':'>'}
openings = ['(', '[', '{', '<']
queue = []
item_price = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
filling_price = {')' : 1, ']' : 2, '}' : 3, '>' : 4}
part1 = 0
part2 = []
for l, line in enumerate(data):
	queue.append([])
	for i, item in enumerate(line):
		#print(f"Queue of line {l}: {queue[-1]}(start)")
		if item in openings:
			queue[l].append(matcher[item])
			if i == len(line) - 1:
				print(f"Line {l} passed: {line}")
				part2_piece = 0
				#print(len(queue[-1]))
				for j in range(len(queue[-1]) - 1, -1, -1):
					print(filling_price[queue[-1][j]])
					part2_piece = part2_piece * 5 + filling_price[queue[-1][j]]
				print(f"Part 2 of line {l}: {part2_piece}.")
				part2.append(part2_piece)				
		elif len(queue[-1]) > 0:
			if queue[-1][-1] == item:
				queue[-1].pop()
				if i == len(line) - 1:
					print(f"Line {l} passed: {line}")
					part2_piece = 0
					#print(len(queue[-1]))
					for j in range(len(queue[-1]) - 1, -1, -1):
						print(filling_price[queue[-1][j]])
						part2_piece = part2_piece * 5 + filling_price[queue[-1][j]]
					print(f"Part 2 of line {l}: {part2_piece}.")
					part2.append(part2_piece)
			else:
				#print(f"Line number {l} done.")
				part1 += item_price[item]
				break
		else:
			#print(f"Line number {l} done.")
			part1 += item_price[item]
			break
		#print(f"Queue of line {l}: {queue[-1]}(end)")
print(part1)
part2.sort()
print(part2[len(part2)//2])