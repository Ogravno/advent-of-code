with open('data.txt') as file:
    rucksacks = file.read().strip().split('\n')

items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def findPriorityOfItems(items):
    priorityOfItems = 0
    for item in items:
        priorityOfItems += findPriorityOfItem(item)
    
    return priorityOfItems

def findPriorityOfItem(item):
    possibleItems = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    item = possibleItems.index(item) + 1
    
    return item


def findMisplacedItems(rucksacks):
    misplacedItems = []
    for rucksack in rucksacks:
        misplacedItems.append(findMisplacedItem(rucksack))

    return misplacedItems


def findMisplacedItem(rucksack):
    misplacedItem = ''

    compartment1 = rucksack[:len(rucksack) // 2]
    compartment2 = rucksack[len(rucksack) // 2:]

    misplacedItem = findMathingItemsInTwoArrays(compartment1, compartment2)[0]

    return misplacedItem

def findMathingItemsInTwoArrays(array1, arrray2):
    matchingItems = []

    for item in array1:
        if item in arrray2:
            matchingItems.append(item)
    
    return matchingItems

def findMatchingItemsInMultipleArrays(arrays):
    matchingItem = ''
    potentialMatchingItems = arrays[0]

    for array in arrays:
        potentialMatchingItems = findMathingItemsInTwoArrays(potentialMatchingItems, array)

    matchingItem = potentialMatchingItems[0]

    return matchingItem

def findGroupBadges(rucksacks):
    groupBadges = []
    for rucksack in rucksacks[::3]:
        group = rucksacks[rucksacks.index(rucksack):rucksacks.index(rucksack) + 3]
        groupBadges.append(findGroupBadge(group))

    return groupBadges

    
def findGroupBadge(group):
    groupBadge = ''
    potentialgroupeBadge = group[0]

    for rucksack in group[1:]:
        potentialgroupeBadge = findMathingItemsInTwoArrays(potentialgroupeBadge, rucksack)

    groupBadge = potentialgroupeBadge[0]

    return groupBadge


misplacedItems = findMisplacedItems(rucksacks)
priorityOfMisplacedItems = findPriorityOfItems(misplacedItems)

groupBadges = findGroupBadges(rucksacks)
priorityofGroupBadges = findPriorityOfItems(groupBadges)



print(f'Misplaced items: {priorityOfMisplacedItems}')
print(f'Group badges: {priorityofGroupBadges}')
