from math import exp, ceil
import copy
import config

#------------------------------------------------------------------------------
#   Function getTotalNums
#    
#   Purpose: Calculate total number of collisions and total number of 
#           same day terms for all students.
#
#   Parameters: 
#       students - Numpy array of student objects.
#
#   Returns: 
#       numOfCollisions - Total number of collisions.
#       numOfSameDayTerms - Total number of same day terms.
#
#------------------------------------------------------------------------------

def getTotalNums(students) -> tuple:
    numOfCollisions = 0
    numOfSameDayTerms = 0
    for s in students:
        numOfCollisions += s.numOfCollisionsForStudent
        numOfSameDayTerms += s.numOfSameDayTerms
    return (numOfCollisions, numOfSameDayTerms)

#------------------------------------------------------------------------------
#   Function setTermForCourse
#    
#   Purpose: Set a new term to a course and to each student of that course. 
#
#   Parameters: 
#       newTerm - Term object which represents new term.
#       course - Course object for which we want to change term.
#
#   Returns: None. Term and student object are modified.
#
#------------------------------------------------------------------------------

def setTermForCourse(newTerm, course) -> None:
    course.term = newTerm
    for s in course.students:
        s.setTerms()

#------------------------------------------------------------------------------
#   Function fastHcCoreAlg
#    
#   Purpose: core code of a fast hill climbing algorithm. For each course 
#           remember the current term of that course and check if any other 
#           term is better. If it is we leave it, if it isn't we change it back. 
#
#   Parameters: 
#       courses - Numpy array of course objects.
#       terms - Numpy array of term objects.
#       students - Numpy array of student objects.
#
#   Returns: 
#       minNumOfCollisions - Minimal number of collisions after iteration.
#       minNumOfSameDayTerms - Minimal number of same day terms after iteration.
#       
#------------------------------------------------------------------------------

def fastHcCoreAlg(courses, terms, students) -> tuple:
    minNumOfCollisions, minNumOfSameDayTerms = getTotalNums(students)
    for courseIndex in range(config.numOfCourses):
        for termIndex in range(config.numOfTerms):
            curTerm = courses[courseIndex].term #current term of current course
            if curTerm.termId != terms[termIndex].termId:
                setTermForCourse(terms[termIndex], courses[courseIndex])
            else:
                continue

            #Calculate numbers of this neighbourhood solution.
            curNumOfCollisions, curNumOfSameDayTerms = getTotalNums(students)

            #If the new solution is better it is the new starting solution.
            #If it is worse, we change back to curTerm.
            if curNumOfCollisions < minNumOfCollisions or (
                curNumOfCollisions == minNumOfCollisions and 
                curNumOfSameDayTerms < minNumOfSameDayTerms):

                minNumOfCollisions = curNumOfCollisions
                minNumOfSameDayTerms = curNumOfSameDayTerms
            else:
                setTermForCourse(curTerm, courses[courseIndex])

    return (minNumOfCollisions, minNumOfSameDayTerms)

#------------------------------------------------------------------------------
#   Function classicHcCoreAlg
#    
#   Purpose: core code of a classic hill climbing algorithm. From current 
#           solution as a starting point, function checks what change to that 
#           solution gives the minimal number of collision and number of same 
#           day terms. Function finds what that change is and makes it happen. 
#           New solution is than starting point of the next iteration.
#
#   Parameters: 
#       courses - Numpy array of course objects.
#       terms - Numpy array of term objects.
#       students - Numpy array of student objects.
#
#   Returns: 
#       minNumOfCollisions - Minimal number of collisions after iteration.
#       minNumOfSameDayTerms - Minimal number of same day terms after iteration.
#       
#------------------------------------------------------------------------------

def classicHcCoreAlg(courses, terms, students) -> tuple:
    minNumOfCollisions, minNumOfSameDayTerms = getTotalNums(students)
    bestCourseIndex = None #index of the best course in courses list to change
    bestTermIndex = None #index of the best term in terms list to change

    for courseIndex in range(config.numOfCourses):
        for termIndex in range(config.numOfTerms):
            curTerm = courses[courseIndex].term #current term of current course
            if curTerm.termId != terms[termIndex].termId:
                setTermForCourse(terms[termIndex], courses[courseIndex])
            else:
                continue

            curNumOfCollisions, curNumOfSameDayTerms = getTotalNums(students)

            #If the new solution is better it is saved,
            # but it is not a new starting solution, we change back to curTerm.
            #If it is worse, we just change back to curTerm.
            if curNumOfCollisions < minNumOfCollisions or (
                curNumOfCollisions == minNumOfCollisions and 
                curNumOfSameDayTerms < minNumOfSameDayTerms):

                minNumOfCollisions = curNumOfCollisions
                minNumOfSameDayTerms = curNumOfSameDayTerms

                bestCourseIndex = courseIndex
                bestTermIndex = termIndex
            setTermForCourse(curTerm, courses[courseIndex])

    if bestCourseIndex != None and bestTermIndex != None:
        setTermForCourse(terms[bestTermIndex], courses[bestCourseIndex])
    return (minNumOfCollisions, minNumOfSameDayTerms)

#------------------------------------------------------------------------------
#   Function hillClimbing
#    
#   Purpose: wrapper code for fast and classic hill climbing algorithms. 
#           If there is no change between two iterations, algorithm is over.
#
#   Parameters: 
#       courses - Numpy array of course objects.
#       terms - Numpy array of term objects.
#       students - Numpy array of student objects.
#
#   Returns: 
#       minNumOfCollisions - Minimal number of collisions after iteration.
#       minNumOfSameDayTerms - Minimal number of same day terms after iteration.
#       
#------------------------------------------------------------------------------

def hillClimbing(courses, terms, students) -> tuple:
    minNumOfCollisions, minNumOfSameDayTerms = getTotalNums(students)

    #We have +1 on next two variables just so we can enter the while loop.
    lastNumOfCollisions = minNumOfCollisions + 1
    lastNumOfSameDayTerms = minNumOfSameDayTerms + 1
    print(minNumOfCollisions, minNumOfSameDayTerms)

    while minNumOfCollisions < lastNumOfCollisions or (
        minNumOfCollisions == lastNumOfCollisions and
        minNumOfSameDayTerms < lastNumOfSameDayTerms):

        lastNumOfCollisions = minNumOfCollisions
        lastNumOfSameDayTerms = minNumOfSameDayTerms
        
        if config.mode == "CHC":
            minNumOfCollisions, minNumOfSameDayTerms = classicHcCoreAlg(courses, terms, students)
        elif config.mode == "FHC":
            minNumOfCollisions, minNumOfSameDayTerms = fastHcCoreAlg(courses, terms, students)

        print(minNumOfCollisions, minNumOfSameDayTerms)
    
    return (minNumOfCollisions, minNumOfSameDayTerms)

#------------------------------------------------------------------------------
#   Function simulatedAnnealing
#    
#   Purpose: Code for a simulated annealing method. In each iteration of main 
#           while loop we decrease current temperature by step, choose one 
#           random solution from neighbourhood of current solution. If it is
#           better, we keep it as a current solution, and if it is worse we still
#           might keep it as a current solution depending on some random factors.
#
#   Parameters: 
#       maxTemp - Integer representing starting temperature of method.
#       minTemp - Integer representing final temperature of method.
#       step - Integer by which we decrease current temperature.
#       courses - Numpy array of course objects.
#       terms - Numpy array of term objects.
#       students - Numpy array of student objects.
#       rng - np.random.default_rng() object for random number generation.
#
#   Returns: 
#       bestCourseIndexs - Numpy array of course objects. Array represents the state
#                   of courses array for the best solution method has found.
#       bestStudents - Numpy array of student objects. Array represents the state
#                   of students array for the best solution method has found.
#       minNumOfCollisions - minimal number of collisions after iteration.
#       minNumOfSameDayTerms - minimal number of same day terms after iteration.
#       
#------------------------------------------------------------------------------

def simulatedAnnealing(maxTemp: int, minTemp: int, step: int, courses, terms, students, rng) -> tuple:
    curTemp = maxTemp
    curNumOfCollisions, curNumOfSameDayTerms = getTotalNums(students)

    minNumOfCollisions = curNumOfCollisions
    minNumOfSameDayTerms = curNumOfSameDayTerms
    bestCourse = copy.deepcopy(courses)
    bestStudents = copy.deepcopy(students)
    uniform = rng.uniform(0, 1, ceil(maxTemp/step))
    k = 0
    if minTemp < 0:
        minTemp = 0

    while curTemp > minTemp:
        #Variables for a random solution we check from neighbourhood
        [randCourseIndex] = rng.integers(config.numOfCourses, size=1)
        [randTermIndex] = rng.integers(config.numOfTerms, size=1)

        curTerm = courses[randCourseIndex].term #current term of current course
        if curTerm != terms[randTermIndex]:
            setTermForCourse(terms[randTermIndex], courses[randCourseIndex])
        else:
            continue
        
        newNumOfCollisions, newNumOfSameDayTerms = getTotalNums(students)

        collisionsDiff = curNumOfCollisions - newNumOfCollisions
        sameDayTermsDiff = curNumOfSameDayTerms - newNumOfSameDayTerms

        #If the bew solution is better we accept it
        if collisionsDiff > 0 or (collisionsDiff == 0 and sameDayTermsDiff > 0):

            if newNumOfCollisions < minNumOfCollisions or (
            newNumOfCollisions == minNumOfCollisions and
            newNumOfSameDayTerms < minNumOfSameDayTerms):
            
                minNumOfCollisions = newNumOfCollisions
                minNumOfSameDayTerms = newNumOfSameDayTerms

                bestCourse = copy.deepcopy(courses)
                bestStudents = copy.deepcopy(students)
                print(minNumOfCollisions, minNumOfSameDayTerms)

        #Check if maybe worse solution will be accepted
        else:
            costDiff = collisionsDiff
            if costDiff == 0:
                costDiff = sameDayTermsDiff

            if uniform[k] > exp(costDiff / curTemp):
                setTermForCourse(curTerm, courses[randCourseIndex])
        k += 1
        curTemp -= step
    
    return (bestCourse, bestStudents, minNumOfCollisions, minNumOfSameDayTerms)