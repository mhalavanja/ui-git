def loadMatrix(fileName: str):
    matrix = []
    with open(fileName) as f:
        lines = f.readlines()
        for line in lines:
            line = line[:-2]
            arr = [int(n) for n in line.split(",")]
            matrix.append(arr)
    return matrix