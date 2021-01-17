import numpy as np
from model import Term, Course, Student
from settings import numOfStudents, numOfCourses, numOfTerms, numOfCoursesPerStudent, numOfTermsPerCourse
from helper import getTotalNumOfCollisions

rng = np.random.default_rng()

terms = np.empty(numOfTerms, dtype=object)
courses = np.empty(numOfCourses, dtype=object)
students = np.empty(numOfStudents, dtype=object)

#Inicijalizacija termina
for i in range(numOfTerms):
    terms[i] = Term(i)

#Odabiranje nasumičnih termina za kolegije
termIdListForCourses = rng.choice(numOfTerms, numOfCourses, replace=True)

#Inicijalizacija kolegija i postavljanje nasumičnih termina
for i in range(numOfCourses):
    courses[i] = Course(i)
    courses[i].term = terms[termIdListForCourses[i]]
    
for i in range(numOfStudents):
    #Incijalizacija studenata
    students[i] = Student(i)

    #Za svakog studenta odaberemo kolegije koje ce upisati
    courseIdListForStudent = rng.choice(numOfCourses, numOfCoursesPerStudent, replace=False)
    curCourses = np.empty(numOfCoursesPerStudent, dtype=object)
    for j in range(numOfCoursesPerStudent):
        #Svakog studenta dodajemo na kolegij koji je upisao
        courses[courseIdListForStudent[j]].appendStudent(students[i])
        curCourses[j] = courses[courseIdListForStudent[j]]
    #Studentu dodajemo sve kolegije koje je upisao 
    students[i].courses = curCourses
    students[i].setTerms()

print(getTotalNumOfCollisions(courses))
