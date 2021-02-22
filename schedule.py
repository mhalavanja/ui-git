import numpy as np
from model import Term, Course, Student
import config
#------------------------------------------------------------------------------
#   Function initilize
#    
#   Purpose: Initialization of required objects. Objects are linked between
#           eachother and input arrays are filled with objects.
#
#   Parameters: 
#       terms - Numpy array of term objects.
#       courses - Numpy array of course objects.
#       students - Numpy array of student objects.
#       rng - np.random.default_rng() object for random number generation.
#
#   Returns: None. Three input arrays are modified.
#
#------------------------------------------------------------------------------

def initilize(terms, courses, students, rng) -> None:
    #Initialization of terms
    for i in range(config.numOfTerms):
        terms[i] = Term(i)

    #Picking a random starting term for each course
    termIdListForCourses = rng.integers(low=0, high=config.numOfTerms, 
                            size=config.numOfCourses)

    #Initialization of each course object and 
    #setting previously picked random term 
    for i in range(config.numOfCourses):
        courses[i] = Course(i)
        courses[i].term = terms[termIdListForCourses[i]]

    #Picking a random number of courses for each student
    numOfCoursesForEachStudent = rng.integers(low=config.minNumOfCoursesPerStudent, 
                                    high=config.maxNumOfCoursesPerStudent, 
                                    size=config.numOfStudents, endpoint=True)

    #Initialization of each student object
    for i in range(config.numOfStudents):
        curNumOfCourses = numOfCoursesForEachStudent[i]
        students[i] = Student(i, curNumOfCourses)

        #For each student we pick random courses they will enrole 
        courseIdListForStudent = rng.choice(config.numOfCourses, 
                                    curNumOfCourses, replace=False)
        curCourses = np.empty(curNumOfCourses, dtype=object)

        #We add each student to the courses they've enrolled
        for j in range(curNumOfCourses):
            courses[courseIdListForStudent[j]].students.append(students[i])
            curCourses[j] = courses[courseIdListForStudent[j]]

        #We set all the courses student enrolled to that student
        students[i].courses = curCourses
        students[i].setTerms()