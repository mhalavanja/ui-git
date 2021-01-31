from math import exp
import config

def getTotalNums(students) -> int:
    numOfCollisions = 0
    numOfSameDayTerms = 0
    for s in students:
        numOfCollisions += s.numOfCollisionsForStudent
        numOfSameDayTerms += s.numOfSameDayTerms
    return (numOfCollisions, numOfSameDayTerms)

#Funkcija koja ce postaviti dani term za course i napraviti sve ostalo sta treba
def setTermForCourse(newTerm, oldTerm, course) -> None:
    oldTerm.courses.remove(course)
    newTerm.courses.append(course)
    course.term = newTerm
    for s in course.students:
        s.setTerms()

def hcCoreAlg(courses, terms, students) -> tuple:
    minNumOfCollisions, minNumOfSameDayTerms = getTotalNums(students)
    for i in range(config.numOfCourses):
        for j in range(config.numOfTerms):
            total = getTotalNums(students)
            assert minNumOfCollisions == total[0]
            assert minNumOfSameDayTerms == total[1]
            oldTerm = courses[i].term
            if oldTerm.termId != terms[j].termId:
                setTermForCourse(terms[j], oldTerm, courses[i])
            else:
                continue

            curNumOfCollisions, curNumOfSameDayTerms = getTotalNums(students)

            if curNumOfCollisions < minNumOfCollisions or (
                curNumOfCollisions == minNumOfCollisions and 
                curNumOfSameDayTerms < minNumOfSameDayTerms):

                minNumOfCollisions = curNumOfCollisions
                minNumOfSameDayTerms = curNumOfSameDayTerms
            else:
                setTermForCourse(oldTerm, terms[j], courses[i])
            pass

    return (minNumOfCollisions, minNumOfSameDayTerms)

def hillClimbing(courses, terms, students) -> tuple:
    curNumOfCollisions, curNumOfSameDayTerms = getTotalNums(students)
    lastNumOfCollisions = curNumOfCollisions + 1
    lastNumOfSameDayTerms = curNumOfSameDayTerms + 1
    bestSolution = {}
    print(curNumOfCollisions, curNumOfSameDayTerms)

    while curNumOfCollisions < lastNumOfCollisions or (
        curNumOfCollisions == lastNumOfCollisions and
        curNumOfSameDayTerms < lastNumOfSameDayTerms):

        lastNumOfCollisions = curNumOfCollisions
        lastNumOfSameDayTerms = curNumOfSameDayTerms
        
        curNumOfCollisions, curNumOfSameDayTerms = hcCoreAlg(courses, terms, students)
        print(curNumOfCollisions, curNumOfSameDayTerms)
    
    for c in courses:
        bestSolution[c.courseId] = c.term.termId
    return (bestSolution, curNumOfCollisions, curNumOfSameDayTerms)

def simulatedAnnealing(maxTemp: int, minTemp: int, step: int, courses, terms, students, rng) -> tuple:
    initialTemp = maxTemp
    finalTemp = minTemp

    curTemp = initialTemp
    curNumOfCollisions, curNumOfSameDayTerms = getTotalNums(courses)

    bestNumOfCollisions = curNumOfCollisions
    bestNumOfSameDayTerms = curNumOfSameDayTerms
    bestSolution = {}

    while curTemp > finalTemp:
        [randCourseIndex] = rng.integers(config.numOfCourses, size=1)
        [randTermIndex] = rng.integers(config.numOfTerms, size=1)

        oldTerm = courses[randCourseIndex].term
        if oldTerm != terms[randTermIndex]:
            setTermForCourse(terms[randTermIndex], oldTerm, courses[randCourseIndex])
        else:
            continue

        newNumOfCollisions, newNumOfSameDayTerms = getTotalNums(courses)

        collisionsDiff = curNumOfCollisions - newNumOfCollisions
        sameDayTermsDiff = curNumOfSameDayTerms - newNumOfSameDayTerms

        if collisionsDiff > 0 or (collisionsDiff == 0 and sameDayTermsDiff > 0):

            if newNumOfCollisions < bestNumOfCollisions or (
            newNumOfCollisions == bestNumOfCollisions and
            newNumOfSameDayTerms < bestNumOfSameDayTerms):
                bestNumOfCollisions = newNumOfCollisions
                bestNumOfSameDayTerms = newNumOfSameDayTerms
                for c in courses:
                    bestSolution[c] = c.term.termId

                print(bestNumOfCollisions, bestNumOfSameDayTerms)

        else:
            costDiff = collisionsDiff
            if costDiff == 0:
                costDiff = sameDayTermsDiff

            if rng.uniform(0, 1, 1) > exp(costDiff / curTemp):
                setTermForCourse(oldTerm, terms[randTermIndex], courses[randCourseIndex])

        curTemp -= step
    
    return (bestSolution, bestNumOfCollisions, bestNumOfSameDayTerms)