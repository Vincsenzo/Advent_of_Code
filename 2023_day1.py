with open("day1data.txt", "r") as f:
	lines = f.read().splitlines()

solution = 0

for w in lines:
	n1 = 0
	n2 = 0
	for char in w:
		if char.isdigit():
			n1 = char
			break
	
	for char in reversed(w):
		if char.isdigit():
			n2 = char
			break
	
	two_digit = int(n1 + n2)
	solution += two_digit

print(solution)