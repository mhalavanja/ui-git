#=============================================================================
#   Assignment:  Project assignment -- Exame Schedule Problem
#
#       Author:  Matija Halavanja
#     Language:  Python 3
#       To Run:  python3 main.py
#
#        Class:  Artificial Intelligence
#   Instructor:  Luka Grubišić
#     Due Date:  25.2.2021.
#
#-----------------------------------------------------------------------------
import numpy as np
import time
import config 
from schedule import initilize
from helper import hillClimbing, simulatedAnnealing

config.setInputData()

rng = None 
if config.seed == "":
    rng = np.random.default_rng()
else:
    rng = np.random.default_rng(int(config.seed))

terms = np.empty(config.numOfTerms, dtype=object)
courses = np.empty(config.numOfCourses, dtype=object)
students = np.empty(config.numOfStudents, dtype=object)

initilize(terms, courses, students, rng)

#Dictionary which is used for validating
studentsTestDict = {} 
for s in students:
    coursesIdList = []
    for c in s.courses:
        coursesIdList.append(c.courseId)
    studentsTestDict[s.studentId] = coursesIdList

#Final number of collisions and same day terms
numOfCollisions = None
numOfSameDayTerms = None

startTime = time.time()
if config.mode == "CHC" or config.mode == "FHC":
    numOfCollisions, numOfSameDayTerms = hillClimbing(courses, terms, students)
elif config.mode == "SA":
    courses, students, numOfCollisions, numOfSameDayTerms = simulatedAnnealing(config.maxTemp, config.minTemp, config.step, courses, terms, students, rng)
elapsedTime = time.time() - startTime

print("Broj kolizija: ", numOfCollisions)
print("Broj ispita na isti dan: ", numOfSameDayTerms)
print("Vrijeme izvršavanja metode: ", elapsedTime, " sekundi")

with open(config.out, "w") as f:    
    for c in courses:
        f.write("{0} {1}\n".format(c.courseId, c.term.termId))

#Code for validating our solution. 
coursesTestDict = {}
for c in courses:
    coursesTestDict[c.courseId] = (c.term.termId, c.term.day)

#Variables which are used for validating
testNumOfCollisions = 0
testNumOfSameDayTerms = 0
for s in students:
    coursesIdList = []
    termsIdList = []
    termsDayList = []
    for c in s.courses:
        coursesIdList.append(c.courseId)
        term = coursesTestDict[c.courseId]
        termsIdList.append(term[0])
        termsDayList.append(term[1])
    testNumOfCollisions += len(s.courses) - len(set(termsIdList))
    testNumOfSameDayTerms += len(s.courses) - len(set(termsDayList))
    assert studentsTestDict[s.studentId] == coursesIdList
    
assert testNumOfCollisions == numOfCollisions
assert testNumOfSameDayTerms == numOfSameDayTerms