from schedule import initilize
import numpy as np
import config 
from helper import hillClimbing, simulatedAnnealing
from schedule import *

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
studentsTestDict = {} 
for s in students:
    coursesIdList = []
    for c in s.courses:
        coursesIdList.append(c.courseId)
    studentsTestDict[s.studentId] = coursesIdList

solution = None
numOfCollisions = None
numOfSameDayTerms = None
if config.mode == "HC":
    solution, numOfCollisions, numOfSameDayTerms = hillClimbing(courses, terms, students)
elif config.mode == "SA":
    solution, numOfCollisions, numOfSameDayTerms = simulatedAnnealing(config.maxTemp, config.minTemp, config.step, courses, terms, students, rng)

print("Broj kolizija: ", numOfCollisions)
print("Broj ispita na isti dan: ", numOfSameDayTerms)
# print("Id kolegija   Id termina")
# for courseId in solution:
#     print(courseId,"            ", solution[courseId])

testNumOfCollisions = 0
testNumOfSameDayTerms = 0
for s in students:
    coursesIdList = []
    s.calculateNumOfCollisionsForStudent
    s.calculateNumOfSameDayTerms
    testNumOfCollisions += s.numOfCollisionsForStudent
    testNumOfSameDayTerms += s.numOfSameDayTerms
    for c in s.courses:
        coursesIdList.append(c.courseId)
    assert studentsTestDict[s.studentId] == coursesIdList
assert testNumOfCollisions == numOfCollisions
assert testNumOfSameDayTerms == numOfSameDayTerms