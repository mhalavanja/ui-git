#-----------------------------------------------------------------------------
#   Function setInputData
#    
#   Purpose: Declearing global variables and collecting
#       user input data.
#-----------------------------------------------------------------------------

def setInputData():
    global numOfStudents
    global numOfCourses
    global numOfTerms
    global numOfTermsPerDay
    global minNumOfCoursesPerStudent
    global maxNumOfCoursesPerStudent
    global seed
    global numOfTerms
    global mode
    global out
    numOfStudents = int(input("Unesite broj studenata: "))
    numOfCourses = int(input("Unesite broj kolegija: "))
    numOfTerms = int(input("Unesite broj termina: "))
    numOfTermsPerDay = int(input("Unesite broj termina po danu: "))
    minNumOfCoursesPerStudent = int(input("Unesite minimalni broj kolegija " +
                                    "koje upisuje student: "))
    maxNumOfCoursesPerStudent = int(input("Unesite maksimalni broj kolegija " +
                                    "koje upisuje student: "))
    seed = input("Unesite seed za generator slučajnih vrijednosti " +
                "ili ostavite prazno: ")
    mode = input('Unesite "CHC" za klasični uspon na vrh, "FHC" za ' +
                'brzi uspon na vrh ili "SA" za simulirano kaljenje: ')
    out = input('Unesite ime izlazne datoteke: ')
    if mode == "CHC" or mode == "FHC":
        return

    global minTemp
    global maxTemp
    global step
    minTemp = None
    maxTemp = None
    step = None
    
    maxTemp = int(input("Unesite maksimalnu (početnu) temperaturu za SA: "))
    minTemp = int(input("Unesite minimalnu (krajnju) temperaturu za SA " +
                        "koja je veća ili jednaka 0: "))
    step = int(input("Unesite korak spuštanja temperature za SA: "))