from pathlib import Path

path = Path(__file__).parent / "../input/day04.txt"
with path.open() as file:
	data = file.read()
data = data.splitlines()
bingo_row = data[0].split(',')
tabs = []
i = -1
for item in data[1:]:
	if len(item) == 0:
		tabs.append([])
		i += 1
		continue
	tabs[i].append(item.split())
#print(tabs)
sum_w = 0
for bingus in bingo_row:
	for i, tab in enumerate(tabs):
		for j, row in enumerate(tab):
			row_c = 0
			for k, num in enumerate(row):
				if num != "X":
					if int(num) == int(bingus):
						row[k] = "X"
						row_c += 1
				else:
					row_c += 1
				if row_c == 5:
					print(f"winner is tab {i}: {tab}")
					for l, row_w in enumerate(tab):
						for m, num_w in enumerate(row_w):
							if num != 'X':
								sum_w += int(num_w)
					sum_w *= int(bingus)
					print(sum_w)			
					exit()
		for j, row in enumerate(tab):
			tab_c = 0
			for k, num in enumerate(row):
				if tab[k][j] == "X":
						tab_c += 1
				if tab_c == 5:
					print(f"First winner is tab {i}: {tab}")
					for l, row_w in enumerate(tab):
						for m, num_w in enumerate(row_w):
							if num_w != 'X':
								sum_w += int(num_w)
								#print(f"num_w: {num_w}, sum_w: {sum_w}")
					sum_w *= int(bingus)
					#print(bingus)
					print(sum_w)
					exit()
print(tabs)
#print(f"winner is tab: {tab}")
#~~COMMENT PART 1 BEFORE USE~~#part2#~~COMMENT PART 1 BEFORE USE~~#
with path.open() as file:
	data = file.read()
data = data.splitlines()
bingo_row = data[0].split(',')
tabs = []
i = -1
for item in data[1:]:
	if len(item) == 0:
		tabs.append([])
		i += 1
		continue
	tabs[i].append(item.split())
#print(tabs)
sum_w = 0
wtabs = []
for bingus in bingo_row:
	for i, tab in enumerate(tabs):
		for j, row in enumerate(tab):
			row_c = 0
			for k, num in enumerate(row):
				if num != "X":
					if int(num) == int(bingus):
						row[k] = "X"
						row_c += 1
				else:
					row_c += 1
				if row_c == 5:
					if i not in wtabs:
						wtabs.append(i)
						if len(wtabs) == len(bingo_row):
							print(f"Last winner is tab {i}: {tab}")
							for l, row_w in enumerate(tab):
								for m, num_w in enumerate(row_w):
									if num_w != 'X':
										sum_w += int(num_w)
										#print(f"num_w: {num_w}, sum_w: {sum_w}")
							sum_w *= int(bingus)
							print(bingus)
							print(sum_w)
							exit()					
		for j, row in enumerate(tab):
			tab_c = 0
			for k, num in enumerate(row):
				if tab[k][j] == "X":
						tab_c += 1
				if tab_c == 5:
					if i not in wtabs:
						wtabs.append(i)
						if len(wtabs) == len(bingo_row):
							print(f"winner is tab {i}: {tab}")
							for l, row_w in enumerate(tab):
								for m, num_w in enumerate(row_w):
									if num_w != 'X':
										sum_w += int(num_w)
										#print(f"num_w: {num_w}, sum_w: {sum_w}")
							sum_w *= int(bingus)
							print(bingus)
							print(sum_w)
							exit()
print(tabs)