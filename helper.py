def getTotalNumOfCollisions(courses) -> int:
    numOfCollisions = 0
    for c in courses:
        c.calculateNumOfCollisionsForCourse()
    for c in courses:
        numOfCollisions += c.numOfCollisionsForCourse
    return numOfCollisions