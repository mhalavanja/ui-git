import numpy as np
from math import exp
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
    return [minNumOfCollisions, minNumOfSameDayTerms]

def hillClimbing(courses, terms, students) -> list:
    minNumOfCollisions = numOfCourses * numOfStudents
    minNumOfSameDayTerms = minNumOfCollisions
    lastNumOfCollisions = 0
    lastNumOfSameDayTerms = 0
    curNumOfCollisions = 1
    curNumOfSameDayTerms = 1
    while lastNumOfCollisions != curNumOfCollisions or lastNumOfSameDayTerms != curNumOfSameDayTerms:
        lastNumOfCollisions = curNumOfCollisions
        lastNumOfSameDayTerms = curNumOfSameDayTerms
        
        curNumOfCollisions, curNumOfSameDayTerms = hcCoreAlg(courses, terms, students)
        print(curNumOfCollisions, curNumOfSameDayTerms)
        if curNumOfCollisions < minNumOfCollisions or (
            curNumOfCollisions <= minNumOfCollisions and
            curNumOfSameDayTerms < minNumOfSameDayTerms):

            minNumOfCollisions = curNumOfCollisions
            minNumOfSameDayTerms = curNumOfSameDayTerms
    
    return curNumOfCollisions, curNumOfSameDayTerms

def simulatedAnnealing(maxTemp: int, minTemp: int, step: int, courses, terms, students) -> list:
    initialTemp = maxTemp
    finalTemp = minTemp

    curTemp = initialTemp
    curNumOfCollisions = getTotalNumOfCollisions(courses)
    curNumOfSameDayTerms = getTotalNumOfSameDayTerms(students)

    bestNumOfCollisions = curNumOfCollisions
    bestNumOfSameDayTerms = curNumOfSameDayTerms
    bestSolution = [courses[:], terms[:], students[:]]

    while curTemp > finalTemp:
        [randCourseIndex] = np.random.randint(0, numOfCourses, 1)
        [randTermIndex] = np.random.randint(0,numOfTerms, 1)

        oldTerm = courses[randCourseIndex].term
        if oldTerm != terms[randTermIndex]:
            setTermForCourse(terms[randTermIndex], oldTerm, courses[randCourseIndex])
        else:
            continue

        newNumOfCollisions = getTotalNumOfCollisions(courses)
        newNumOfSameDayTerms = getTotalNumOfSameDayTerms(students)

        collisionsDiff = curNumOfCollisions - newNumOfCollisions
        sameDayTermsDiff = curNumOfSameDayTerms - newNumOfSameDayTerms

        if collisionsDiff > 0 or (collisionsDiff == 0 and sameDayTermsDiff > 0):

            if newNumOfCollisions < bestNumOfCollisions or (
            newNumOfCollisions == bestNumOfCollisions and
            newNumOfSameDayTerms < bestNumOfSameDayTerms):
                bestNumOfCollisions = newNumOfCollisions
                bestNumOfSameDayTerms = newNumOfSameDayTerms
                bestSolution[0] = courses[:]
                bestSolution[1] = terms[:]
                bestSolution[2] = students[:]

                print(bestNumOfCollisions, bestNumOfSameDayTerms)

        else:
            costDiff = collisionsDiff
            if costDiff == 0:
                costDiff = sameDayTermsDiff

            if np.random.random_sample() > exp(costDiff / curTemp):
                setTermForCourse(oldTerm, terms[randTermIndex], courses[randCourseIndex])

        curTemp -= step
    
    return bestSolution

