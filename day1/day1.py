with open('data.txt') as file:
    items = file.read().strip().split('\n')

elfs = []
nextElf = 0

for calInItem in items:
    if calInItem == '':
        elfs.append(nextElf)
        nextElf = 0
    else:
        nextElf += int(calInItem)
        
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