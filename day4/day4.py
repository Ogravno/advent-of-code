with open("data.txt", "r") as f:
    data = [line.rstrip('\n').split(',') for line in f.readlines()]

def format_data(data):
    assignmentPairs = []
    for assignmentPair in data:
        firstAssignment, secondAssignment = string_to_range(assignmentPair[0]), string_to_range(assignmentPair[1])
        assignmentPairObject = AssignmentPair(firstAssignment, secondAssignment)
        assignmentPairs.append(assignmentPairObject)

    return assignmentPairs
 
def string_to_range(s):
    start, end = map(int, s.split('-'))
    return range(start, end + 1)

def ranges_fully_contain(range1, range2):
    return range1.start <= range2.start and range1.stop - 1 >= range2.stop - 1

def ranges_overlapping(range1, range2):
    return range1.start <= range2.stop - 1 and range1.stop - 1 >= range2.start

def find_number_of_fully_contained_pairs(assignmentPairs):
    numberOfFullyContainedPairs = 0
    for assignmentPair in assignmentPairs:
        assignment1 = assignmentPair.getFirstAssignment()
        assignment2 = assignmentPair.getSecondAssignment()

        if ranges_fully_contain(assignment1, assignment2) or ranges_fully_contain(assignment2, assignment1):
            numberOfFullyContainedPairs += 1
    
    return numberOfFullyContainedPairs

def find_number_of_overlapping_pairs(assignmentPairs):
    numberOfOverlappingPairs = 0
    for assignmentPair in assignmentPairs:
        assignment1 = assignmentPair.getFirstAssignment()
        assignment2 = assignmentPair.getSecondAssignment()

        if ranges_overlapping(assignment1, assignment2):
            numberOfOverlappingPairs += 1
    
    return numberOfOverlappingPairs

class AssignmentPair:
    def __init__(self, firstAssignment, secondAssignment):
        self.firstAssignment = firstAssignment
        self.secondAssignment = secondAssignment
    
    def getFirstAssignment(self):
        return self.firstAssignment
    
    def getSecondAssignment(self):
        return self.secondAssignment

assignmentPairs = format_data(data)

numberOfFullyContainedPairs = find_number_of_fully_contained_pairs(assignmentPairs)
numberOfOverlappingPairs = find_number_of_overlapping_pairs(assignmentPairs)

print('fully contained:', numberOfFullyContainedPairs)
print('overlapping:', numberOfOverlappingPairs)