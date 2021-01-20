import numpy as np
from model import Term, Course, Student
from settings import numOfStudents, numOfCourses, numOfTerms, numOfCoursesPerStudent#, maxNumOfStudentsPerTerm
from helper import getTotalNumOfCollisions, getTotalNumOfSameDayTerms, hillClimbing#, getTotalNumOfOverCapacity
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
    courses[i].term.courses.append(courses[i])
    
numOfCoursesForEachStudent = rng.choice(np.arange(1, numOfCoursesPerStudent), numOfStudents)
for i in range(numOfStudents):
    #Incijalizacija studenata
    curNumOfCourses = numOfCoursesForEachStudent[i]
    students[i] = Student(i, curNumOfCourses)
    #Za svakog studenta odaberemo kolegije koje ce upisati
    courseIdListForStudent = rng.choice(numOfCourses, curNumOfCourses, replace=False)
    curCourses = np.empty(curNumOfCourses, dtype=object)
    for j in range(curNumOfCourses):
        #Svakog studenta dodajemo na kolegij koji je upisao
        courses[courseIdListForStudent[j]].appendStudent(students[i])
        curCourses[j] = courses[courseIdListForStudent[j]]
    #Studentu dodajemo sve kolegije koje je upisao 
    students[i].courses = curCourses
    students[i].setTerms()

for t in terms:
    t.calculateNumOfStudentsInTerm()
    # terms[i].calculateOverCapacity()

for c in courses:
    c.calculateNumOfCollisionsForCourse()

print(getTotalNumOfCollisions(courses), getTotalNumOfSameDayTerms(students)) #+ getTotalNumOfOverCapacity(terms))

# finalNumOfCollisions, finalCourses = hillClimbing1(courses, terms)
minCol = numOfCourses * numOfStudents
minNum = minCol
lastNumOfCollisions = 0
lastNumOfSameDayTerms = 0
curNumOfCollisions = 1
curNumOfSameDayTerms = 1
while lastNumOfCollisions != curNumOfCollisions or lastNumOfSameDayTerms != curNumOfSameDayTerms:
    lastNumOfCollisions = curNumOfCollisions
    lastNumOfSameDayTerms = curNumOfSameDayTerms
    curNumOfCollisions, curNumOfSameDayTerms, curCourses = hillClimbing(courses, terms, students)
    print(curNumOfCollisions, curNumOfSameDayTerms)
    if curNumOfCollisions < minCol or (
        curNumOfCollisions <= minCol and
        curNumOfSameDayTerms < minNum):

        minCol = curNumOfCollisions
        minNum = curNumOfSameDayTerms
