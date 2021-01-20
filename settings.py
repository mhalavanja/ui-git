from math import ceil

#broj studenata
numOfStudents = 800
# numOfStudents = 5

#broj ispita
numOfCourses = 72
# numOfCourses = 2

#broj termina u kojima se mogu odvijati ispiti
numOfTerms = 42
# numOfTerms = 2

#broj termina za pisanje ispita u jednom danu
numOfTermsPerDay = 3

#broj dana za pisanje ispita
numOfDays = ceil(numOfTerms / numOfTermsPerDay)

#broj kolegija po studentnu
numOfCoursesPerStudent = 5
