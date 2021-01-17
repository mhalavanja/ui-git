import numpy as np
from settings import numOfTermsPerCourse, numOfCoursesPerStudent, maxNumOfStudentsPerTerm

class Course:
    def __init__(self, courseId: int) -> None:
        self.courseId = courseId
        self.students = []
        self.term = None
        self.numOfCollisionsForCourse = -1
        self.numOfStudents = 0
        
    # def setStudents(self, students) -> None:
    #     self.students = students
    #     self.numOfStudents = len(students)
    
    def appendStudent(self, student) -> None:
        self.students.append(student)
        self.numOfStudents += 1

    def setTerm(self, term):
        self.term = term    
        self.calculateNumOfCollisionsForCourse()

    def calculateNumOfCollisionsForCourse(self) -> None:
        collisions = 0
        for s in self.students:
            collisions += s.numOfCollisionsForStudent
        self.numOfCollisionsForCourse = collisions

class Student:
    def __init__(self, studentId: int) -> None:
        self.studentId = studentId
        self.courses = np.empty(numOfCoursesPerStudent, dtype=object)
        self.terms = np.empty_like(self.courses)
        self.numOfCollisionsForStudent = -1

    def setCourses(self, courses):
        self.courses = courses
        self.setTerms()

    def setTerms(self) -> None:
        for i in range(numOfCoursesPerStudent):
            self.terms[i] = self.courses[i].term
        self.calculateNumOfCollisionsForStudent()

    def calculateNumOfCollisionsForStudent(self) -> None:
        collisions = numOfCoursesPerStudent - len(set(self.terms))
        self.numOfCollisionsForStudent = collisions


class Term:
    def __init__(self, termId) -> None:
        self.termId = termId
        self.courses = None
        self.numOfStudentsInTerm = -1

    def setCourses(self, courses) -> None:
        self.courses = courses
        self.calculateNumOfStudentsInTerm()

    def calculateNumOfStudentsInTerm(self) -> None:
        num = 0
        for c in self.courses:
            num += c.numOfStudents
        self.numOfStudentsInTerm = num
