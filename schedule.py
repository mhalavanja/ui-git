import numpy as np
from model import Term, Course, Student
import config

def initilize(terms, courses, students, rng):
    #Inicijalizacija termina
    for i in range(config.numOfTerms):
        terms[i] = Term(i)

    #Odabiranje nasumičnih termina za kolegije
    termIdListForCourses = rng.integers(low=0, high=config.numOfTerms, size=config.numOfCourses)

    #Inicijalizacija kolegija i postavljanje nasumičnih termina
    for i in range(config.numOfCourses):
        courses[i] = Course(i)
        courses[i].term = terms[termIdListForCourses[i]]
        courses[i].term.courses.append(courses[i])
    
    numOfCoursesForEachStudent = rng.integers(low=config.minNumOfCoursesPerStudent, high=config.maxNumOfCoursesPerStudent, size=config.numOfStudents, endpoint=True)
    for i in range(config.numOfStudents):
        #Incijalizacija studenata
        curNumOfCourses = numOfCoursesForEachStudent[i]
        students[i] = Student(i, curNumOfCourses)
        #Za svakog studenta odaberemo kolegije koje ce upisati
        courseIdListForStudent = rng.choice(config.numOfCourses, curNumOfCourses, replace=False)
        curCourses = np.empty(curNumOfCourses, dtype=object)
        for j in range(curNumOfCourses):
            #Svakog studenta dodajemo na kolegij koji je upisao
            courses[courseIdListForStudent[j]].students.append(students[i])
            curCourses[j] = courses[courseIdListForStudent[j]]
        #Studentu dodajemo sve kolegije koje je upisao 
        students[i].courses = curCourses
        students[i].setTerms()

    for c in courses:
        c.numOfStudents = len(c.students)