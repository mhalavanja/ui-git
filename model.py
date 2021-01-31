import numpy as np
import config

class Course:
    def __init__(self, courseId: int) -> None:
        self.courseId = courseId
        self.term = None
        self.students = []
        self.numOfStudents = 0
        self.numOfCollisionsForCourse = -1
        
    def appendStudent(self, student) -> None:
        self.students.append(student)
        self.numOfStudents += 1

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
        self.numOfCourses = numOfCoursesForStudent
        self.numOfCollisionsForStudent = -1
        self.numOfSameDayTerms = -1

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
        self.day = termId // config.numOfTermsPerDay

    def calculateNumOfStudentsInTerm(self) -> None:
        num = 0
        for c in self.courses:
            num += c.numOfStudents
        self.numOfStudentsInTerm = num