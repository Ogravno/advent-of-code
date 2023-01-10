with open('data.txt') as file:
    data = file.read().strip().split('\n')

elfs = []
nextElf = 0

for x in data:
    if x == '':
        elfs.append(nextElf)
        nextElf = 0
    else:
        nextElf += int(x)
        
elfs.append(nextElf)

#sorts the list of elfs
elfs.sort(reverse=True)
print(elfs)

#finds the three elfs carrying the most calories
top3Elfs = elfs[0:3]
print('\ntop 3 elfs:\n' + str(top3Elfs))

#shows the result
result = sum(top3Elfs)
print('\nresult:\n' + str(result))