from settings import numOfCourses, numOfTerms

def getTotalNumOfCollisions(courses) -> int:
    numOfCollisions = 0
    for c in courses:
        numOfCollisions += c.numOfCollisionsForCourse
    return numOfCollisions

# def getTotalNumOfOverCapacity(terms):
#     num = 0
#     for t in terms:
#         num += t.overCapacity
#     return num

def swapTermsInStudents(course1, course2):
    for s in course1.students:
        s.setTerms()
        pass
        # s.calculateNumOfCollisionsForStudent()
    for s in course2.students:
        s.setTerms()
        # s.calculateNumOfCollisionsForStudent()


def swapCoursesInTerms(term1, index1: int, term2, index2: int):
    tempCourse = term1.courses[index1]
    term1.courses[index1] = term2.courses[index2]
    term2.courses[index2] = tempCourse
    
    term1.calculateNumOfStudentsInTerm()
    term2.calculateNumOfStudentsInTerm()
    
    # term1.calculateOverCapacity()
    # term2.calculateOverCapacity()

def swapTermsInCourses(courses, i: int, j: int):
        index1 = courses[i].term.courses.index(courses[i])
        index2 = courses[j].term.courses.index(courses[j])
        swapCoursesInTerms(courses[i].term, index1, courses[j].term, index2)
        
        tempTerm = courses[j].term
        courses[j].term = courses[i].term
        courses[i].term = tempTerm

        swapTermsInStudents(courses[i], courses[j])

        courses[i].calculateNumOfCollisionsForCourse()
        courses[j].calculateNumOfCollisionsForCourse()
        

def hillClimbing1(courses, terms):
    numOfCollisions = getTotalNumOfCollisions(courses)
    # numOfOverCapacity = getTotalNumOfOverCapacity(terms)
    minHeuristic = numOfCollisions# + numOfOverCapacity
    i = 0
    while i < numOfCourses:
        newMin = False
        for j in range(i + 1, numOfCourses):
            if courses[j].term != courses[i].term:
                swapTermsInCourses(courses, i, j)
            else:
                continue
            # curNumOfOverCapacity = getTotalNumOfOverCapacity(terms)
            curNumOfCollisions = getTotalNumOfCollisions(courses)
            curHeuristic = curNumOfCollisions# + curNumOfOverCapacity
            if curHeuristic < minHeuristic:
                minHeuristic = curHeuristic
                newMin = True
                break
            else:
                swapTermsInCourses(courses, i, j)
        if not newMin:
            i += 1
    return (minHeuristic, courses)

def hillClimbing(courses, terms):
    minNumOfCollisions = getTotalNumOfCollisions(courses)
    i = 0
    while i < numOfCourses:
        newMin = False
        for j in range(numOfTerms):
            curTerm = courses[i].term
            if curTerm != terms[j]:
                courses[i].term = terms[j]
                for s in courses[i].students:
                    s.setTerms()
                courses[i].calculateNumOfCollisionsForCourse()
            else:
                continue
            curNumOfCollisions = getTotalNumOfCollisions(courses)
            if curNumOfCollisions < minNumOfCollisions:
                minNumOfCollisions = curNumOfCollisions
                newMin = True
                break
            else:
                courses[i].term = curTerm
                for s in courses[i].students:
                    s.setTerms()
                courses[i].calculateNumOfCollisionsForCourse()
        if not newMin:
            i += 1
    return (minNumOfCollisions, courses)