from pathlib import Path

path = Path(__file__).parent / "../input/day08.txt"
with path.open() as file:
	data = file.read()
scrambled_data = [digits.split(" | ")[1].split(" ") for digits in data.splitlines()]
print(scrambled_data)
data = [digits.split(" | ")[0].split(" ") for digits in data.splitlines()]
#print(data)
filter = {2 : 1, 3 : 7, 4 : 4, 7 : 8}
empty_pattern = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
exclusion_list = {'a' : [5, 6], 'b' : [2], 'c' : [1, 4, 7], 'd' : [1, 4], 'e' : [1, 2, 3, 7], 'f' : [0, 1, 7], 'g' : [1, 3, 4, 5, 7, 9]}
part1 = 0
part2 = 0
for sets in data:
	for digit in sets:
		if len(digit) in filter:
			part1 += 1
#print(part1)
for sets in range(len(data)):
	#print(f"New line: {data[sets]}")
	#num = ""
	#translator = {'a' : "", 'b' : "", 'c' : "", 'd' : "", 'e' : "", 'f' : "", 'g' : ""}
	#letter_set = []
#For one, four, seven, eight
	set690 = []
	set235 = []
	for nums in range(len(data[sets])):
		if len(data[sets][nums]) == 2:
			one = "".join(sorted(data[sets][nums]))
			print(f"One check: {one}.")
		elif len(data[sets][nums]) == 3:
			seven = "".join(sorted(data[sets][nums]))
			print(f"Seven check: {seven}.")
		elif len(data[sets][nums]) == 4:
			four = "".join(sorted(data[sets][nums]))
			print(f"Four check: {four}.")
		elif len(data[sets][nums]) == 7:
			eight = "".join(sorted(data[sets][nums]))
			print(f"Eight check: {eight}.")
		elif len(data[sets][nums]) == 6:
			set690.append(data[sets][nums])
			#print(f"Set 6-9-0 check: {set690}.")
		elif len(data[sets][nums]) == 5:
			set235.append(data[sets][nums])
			#print(f"Set 2-3-5 check: {set235}.")
#For six nine zero
	for x in set690:
		is_six_count = 0
		for letter in x:
			if letter in one:
				is_six_count += 1
		if is_six_count == 1:
			six = x		
			print(f"Six check: {six}.")																#SIX~666
			set690.remove(x)
			#print(f"Set 6-9-0 has changed: {set690}.")
			break
	for x in set690:
		for i in four:
			if i not in x:
				#translator['f'] = i
				zero = x
				print(f"Zero check: {zero}.")														#ZERO~000
				set690.remove(x)
				nine = "".join(sorted(set690[0]))
				print(f"Nine check: {nine}.")
#For two three fife
	for x in set235:
		is_three_count = 0
		for letter in x:
			if letter in seven:
				is_three_count += 1
		if is_three_count == 3:
			three = x
			print(f"Three check: {three}.")															#THREE~333
			set235.remove(x)
			break
	for x in set235:
		is_five_count = 0
		for i in four:
			if i in x:
				is_five_count += 1
		if is_five_count == 3:
			five = x
			print(f"Five check: {five}.")															#FIVE~555
			set235.remove(x)
			two = "".join(sorted(set235[0]))														#TWO~222
			print(f"Two check: {two}.")
	mask_pack = ["".join(sorted(zero)), one, two, "".join(sorted(three)), four, "".join(sorted(five)), "".join(sorted(six)), seven, eight, nine]
	print(f"Iteration {sets} masks: {mask_pack}")
	val = ""
	for digit in scrambled_data[sets]:
		for m, mask in enumerate(mask_pack):
			loc_num = "".join(sorted(digit))
			if mask == loc_num:
				print(f"Mask/Number:  {mask} || {loc_num}.")
				val += str(m)

	part2 += int(val)
	print(f"Iteration {sets} value: {part2}")
	

print(part2)
"""
{a : [0, 1, 2, 3, 4, 7, 8, 9], 
b : [0, 1, 3, 4, 5, 6, 7, 8, 9], 
c : [0, 2, 3, 5, 6, 8, 9], 
d : [0, 2, 3, 5, 6, 7, 8, 9], 
e : [0, 4, 5, 6, 8, 9], 
f : [2, 3, 4, 5, 6, 8, 9], 
g : [0, 2, 6, 8]}

{a : [5, 6], b : [2], c : [1, 4, 7], d : [1, 4], e : [1, 2, 3, 7], f : [0, 1, 7], g : [1, 3, 4, 5, 7, 9]}"""

#For letter A
"""	for x in seven:
		if x not in whattt[0]:
			translator['a'] = x"""
