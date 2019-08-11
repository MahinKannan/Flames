name1 = list((input("Enter first name: ")).lower())
name2 = list((input("Enter second name: ")).lower())
unmatched_letters = 0

for i in range(len(name1)):
	for j in range(len(name2)):
		if name1[i] == name2[j]:
			name1[i] = '*'
			name2[j] = '*'
for i in range(len(name1)):
	if name1[i] != '*':
		unmatched_letters += 1
for i in range(len(name2)):
	if name2[i] != '*':
		unmatched_letters += 1
print(unmatched_letters)
flames = ['F', 'L', 'A', 'M', 'E', 'S']

while(len(flames)) > 1:
	rem = unmatched_letters % len(flames)
	if rem == 0:
		rem == len(flames) - 1
	del flames[rem-1]
print(flames)