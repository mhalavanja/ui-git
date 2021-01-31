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
    numOfStudents = 1600
    numOfCourses = 72
    numOfTerms = 42
    numOfTermsPerDay = 3
    minNumOfCoursesPerStudent = 1
    maxNumOfCoursesPerStudent = 5
    seed = ""
    mode = "HC"
    # numOfStudents = int(input("Unesite broj studenata: "))
    # numOfCourses = int(input("Unesite broj kolegija: "))
    # numOfTerms = int(input("Unesite broj termina: "))
    # numOfTermsPerDay = int(input("Unesite broj termina po danu: "))
    # minNumOfCoursesPerStudent = int(input("Unesite minimalni broj kolegija koje upisuje student: "))
    # maxNumOfCoursesPerStudent = int(input("Unesite maksimalni broj kolegija koje upisuje student: "))
    # seed = input("Unesite seed za generator slučajnih vrijednosti ili ostavite prazno: ")
    # mode = input('Unesite "HC" za hill climbing ili "SA" za simulated annealing: ')
    if mode == "HC":
        return

    global minTemp
    global maxTemp
    global step
    minTemp = 0
    maxTemp = 100000
    step = 1
    # minTemp = None
    # maxTemp = None
    # step = None
    
    # maxTemp = int(input("Unesite maksimalnu (početnu) temperaturu za SA: "))
    # minTemp = int(input("Unesite minimalnu (krajnju) temperaturu za SA: "))
    # step = int(input("Unesite korak spuštanja temperature za SA: "))