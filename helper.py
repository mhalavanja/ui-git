from settings import numOfCourses, numOfTerms, numOfStudents

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
def setTermForCourse(newTerm, oldTerm, course) -> None:
    oldTerm.courses.remove(course)
    oldTerm.calculateNumOfStudentsInTerm()
    newTerm.courses.append(course)
    newTerm.calculateNumOfStudentsInTerm()
    course.term = newTerm
    for s in course.students:
        s.setTerms()
    course.calculateNumOfCollisionsForCourse()

def hcCoreAlg(courses, terms, students) -> list:
    minNumOfCollisions = getTotalNumOfCollisions(courses)
    minNumOfSameDayTerms = getTotalNumOfSameDayTerms(students)
    i = 0
    while i < numOfCourses:
        newMin = False
        for j in range(numOfTerms):
            oldTerm = courses[i].term
            if oldTerm != terms[j]:
                setTermForCourse(terms[j], oldTerm, courses[i])
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
                setTermForCourse(oldTerm, terms[j], courses[i])
        if not newMin:
            i += 1
    return [minNumOfCollisions, minNumOfSameDayTerms, courses]

def hillClimbing(courses, terms, students) -> list:
    minCol = numOfCourses * numOfStudents
    minNum = minCol
    lastNumOfCollisions = 0
    lastNumOfSameDayTerms = 0
    curNumOfCollisions = 1
    curNumOfSameDayTerms = 1
    while lastNumOfCollisions != curNumOfCollisions or lastNumOfSameDayTerms != curNumOfSameDayTerms:
        lastNumOfCollisions = curNumOfCollisions
        lastNumOfSameDayTerms = curNumOfSameDayTerms
        curNumOfCollisions, curNumOfSameDayTerms, curCourses = hcCoreAlg(courses, terms, students)
        print(curNumOfCollisions, curNumOfSameDayTerms)
        if curNumOfCollisions < minCol or (
            curNumOfCollisions <= minCol and
            curNumOfSameDayTerms < minNum):

            minCol = curNumOfCollisions
            minNum = curNumOfSameDayTerms