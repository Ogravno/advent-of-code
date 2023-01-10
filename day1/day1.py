with open('./data.txt') as file:
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

elfs.sort()

print(elfs)

result = max(elfs)

print(result)