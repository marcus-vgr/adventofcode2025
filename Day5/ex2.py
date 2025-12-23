def getInput(filename: str) -> list[list[int]]:
    with open(filename, "r") as f:
        lines = f.readlines()
    
    freshIDRanges = []
    for line in lines:
        line = line.strip()
        if len(line) < 1: break
        if "-" in line:
            i,f = line.split("-")
            freshIDRanges.append([int(i), int(f)])

    return freshIDRanges


def solution(freshIDRanges: list[list[int]]) -> int:

    # lets first sort the ranges based on RangeInitial
    freshIDRanges = sorted(freshIDRanges, key = lambda x: x[0])
    #uniqueIDs = [] # This is just to debug
    nFresh = 0

    RI, RF = freshIDRanges[0]
    nFresh += RF - RI + 1
    #uniqueIDs = uniqueIDs + list(range(RI, RF+1))
    for i in range(1, len(freshIDRanges)):
        ri, rf = freshIDRanges[i]
        if ri > RF: # No overlap
            nFresh += rf - ri + 1
            #uniqueIDs = uniqueIDs + list(range(ri, rf+1))
            RI, RF = ri, rf
        else:
            if rf > RF:
                nFresh += rf - RF # dont count RF!
                #uniqueIDs = uniqueIDs + list(range(RF+1, rf+1))
                RI, RF = ri, rf

    #print(uniqueIDs)
    #assert nFresh == len(uniqueIDs)
    return nFresh


if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test: ", solution(test))

    final = getInput("input.txt")
    print("Solution final: ", solution(final))