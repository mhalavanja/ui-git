from settings import numOfCourses, numOfTerms

def getTotalNumOfCollisions(courses) -> int:
    numOfCollisions = 0
    for c in courses:
        numOfCollisions += c.numOfCollisionsForCourse
    return numOfCollisions

def getTotalNumOfSameDayTerms(students) -> int:
    numOfSameDayTerms = 0
    for s in students:
        numOfSameDayTerms += s.numOfSameDayTerms
    return numOfSameDayTerms

# def getTotalNumOfOverCapacity(terms):
#     num = 0
#     for t in terms:
#         num += t.overCapacity
#     return num

#Funkcija koja ce postaviti dani term za course i napraviti sve ostalo sta treba
def setTermForCourse():
    pass

def hillClimbing(courses, terms, students):
    minNumOfCollisions = getTotalNumOfCollisions(courses)
    minNumOfSameDayTerms = getTotalNumOfSameDayTerms(students)
    i = 0
    while i < numOfCourses:
        newMin = False
        for j in range(numOfTerms):
            curTerm = courses[i].term
            if curTerm != terms[j]:
                curTerm.courses.remove(courses[i])
                curTerm.calculateNumOfStudentsInTerm()
                terms[j].courses.append(courses[i])
                terms[j].calculateNumOfStudentsInTerm()
                courses[i].term = terms[j]
                for s in courses[i].students:
                    s.setTerms()
                courses[i].calculateNumOfCollisionsForCourse()
            else:
                continue
            curNumOfCollisions = getTotalNumOfCollisions(courses)
            curNumOfSameDayTerms = getTotalNumOfSameDayTerms(students)
            if curNumOfCollisions < minNumOfCollisions or (
                curNumOfCollisions <= minNumOfCollisions and 
                curNumOfSameDayTerms < minNumOfSameDayTerms):

                minNumOfCollisions = curNumOfCollisions
                minNumOfSameDayTerms = curNumOfSameDayTerms
                newMin = True
            else:
                curTerm.courses.append(courses[i])
                curTerm.calculateNumOfStudentsInTerm()
                terms[j].courses.remove(courses[i])
                terms[j].calculateNumOfStudentsInTerm()
                courses[i].term = curTerm
                for s in courses[i].students:
                    s.setTerms()
                courses[i].calculateNumOfCollisionsForCourse()
        if not newMin:
            i += 1
    return (minNumOfCollisions, minNumOfSameDayTerms, courses)