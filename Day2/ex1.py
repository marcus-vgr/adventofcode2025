def getInput(filename: str) -> list[list[int]]:
    with open(filename, "r") as f:
        o = f.readlines()[0].strip()
    l = o.split(",")
    l = [ll.split("-") for ll in l]
    l = [[int(ll[0]), int(ll[1])] for ll in l]
    return l

def isInvalid(s: str) -> bool:
    N = len(s)
    
    if N % 2 != 0:
        return False
    
    """ # Original version is simpler. Just repeat twice
    for maxidx in range(1, int(N / 2)+1):
        seq = s[:maxidx]
        if s.count(seq) * len(seq) == N:
            return True
    """
    seq = s[:N//2]
    if s.count(seq) == 2:
        return True    
    return False

def solution(idIntervals: list[list[int]]) -> int:

    invalidIDs = []
    for idInterval in idIntervals:
        firstID, finalID = idInterval
        for id in range(firstID, finalID+1):
            if isInvalid(str(id)):
                invalidIDs.append(id)

    print(invalidIDs)
    return sum(invalidIDs)


if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test: ", solution(test))
    
    final = getInput("input.txt")
    print("Solution final: ", solution(final))