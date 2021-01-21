import numpy as np
from settings import numOfTermsPerDay#, maxNumOfStudentsPerTerm

class Course:
    def __init__(self, courseId: int) -> None:
        self.courseId = courseId
        self.students = []
        self.term = None
        self.numOfCollisionsForCourse = -1
        self.numOfStudents = 0
        
    def appendStudent(self, student) -> None:
        self.students.append(student)
        self.numOfStudents += 1

    def setTerm(self, term):
        self.term = term    
        self.calculateNumOfCollisionsForCourse()

    def calculateNumOfCollisionsForCourse(self) -> None:
        collisions = 0
        for s in self.students:
            if s.numOfCollisionsForStudent > 0:
                collisions += 1
        self.numOfCollisionsForCourse = collisions

class Student:
    def __init__(self, studentId: int, numOfCoursesForStudent) -> None:
        self.studentId = studentId
        self.courses = np.empty(numOfCoursesForStudent, dtype=object)
        self.terms = np.empty_like(self.courses)
        self.numOfCollisionsForStudent = -1
        self.numOfCourses = numOfCoursesForStudent
        self.numOfSameDayTerms = -1

    def setCourses(self, courses):
        self.courses = courses
        self.setTerms()

    def setTerms(self) -> None:
        for i in range(self.numOfCourses):
            self.terms[i] = self.courses[i].term
        self.calculateNumOfCollisionsForStudent()
        self.calculateNumOfSameDayTerms()

    def calculateNumOfCollisionsForStudent(self) -> None:
        collisions = self.numOfCourses - len(set(self.terms))
        self.numOfCollisionsForStudent = collisions
    
    def calculateNumOfSameDayTerms(self) -> None:
        termsDays = set()
        for t in self.terms:
            termsDays.add(t.day)
        self.numOfSameDayTerms = self.numOfCourses - len(termsDays)


class Term:
    def __init__(self, termId) -> None:
        self.termId = termId
        self.courses = []
        self.numOfStudentsInTerm = -1
        self.day = termId // numOfTermsPerDay
        # self.overCapacity = -1

    def setCourses(self, courses) -> None:
        self.courses = list(courses)
        self.calculateNumOfStudentsInTerm()

    def calculateNumOfStudentsInTerm(self) -> None:
        num = 0
        for c in self.courses:
            num += c.numOfStudents
        self.numOfStudentsInTerm = num

    # def calculateOverCapacity(self) -> None:
    #     if self.numOfStudentsInTerm > maxNumOfStudentsPerTerm:
    #         self.overCapacity = self.numOfStudentsInTerm - maxNumOfStudentsPerTerm
    #     else:
    #         self.overCapacity = 0