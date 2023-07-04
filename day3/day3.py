with open('data.txt') as file:
    rucksacks = file.read().strip().split('\n')

items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

totalPriority = 0
for rucksack in rucksacks:
    compartment1 = rucksack[:len(rucksack) // 2]
    compartment2 = rucksack[len(rucksack) // 2:]
    
    misplacedItem = ''

    for item in compartment1:
        if item in compartment2:
            misplacedItem = item

    priorityOfItem = items.index(misplacedItem) + 1
    totalPriority += priorityOfItem

print(totalPriority)
