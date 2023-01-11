with open('data.txt') as file:
    data = file.read().strip().split('\n')

def findWinner(letter):
    match letter:
        case 'X':
            return 'lose'
        case 'Y':
            return 'draw'
    
    return 'win'

def findOpponentShape(letter):
    letters = ['A', 'B', 'C']
    shapes = ['rock', 'paper', 'scissors']

    index = letters.index(letter)
    shape = shapes[index]

    return shape

def findMyShape(opponentShape, result):
    if result == 'draw':
        return opponentShape
    
    shapes = ['rock', 'paper', 'scissors']

    match result:
        case 'win':
            index = shapes.index(opponentShape) + 1
        case 'lose':
            index = shapes.index(opponentShape) - 1
    
    if index >= len(shapes):
        index = 0
    elif index <= -1:
        index = len(shapes) - 1

    return shapes[index]


totalPoints = 0

for round in data: 
    opponentShape = findOpponentShape(round[0])
    result = findWinner(round[2])
    myShape = findMyShape(opponentShape, result)

    points = 0
    match myShape:
        case 'rock':
            points += 1
        case 'paper':
            points += 2
        case 'scissors':
            points += 3
    
    match result:
        case 'win':
            points += 6
        case 'draw':
            points += 3
    
    totalPoints += points

print(totalPoints)