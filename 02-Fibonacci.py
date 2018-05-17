sequence = [1,2]
sum = 0
for x in range(2, 1000):
	sequence.append(sequence[x - 1] + sequence[x - 2])
	if sequence[x] >= 4000000:
		break
for x in sequence:
	if x % 2 == 0:
		sum += x
print(sum)