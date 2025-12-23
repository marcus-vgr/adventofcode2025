def getInput(filename: str) -> tuple[list[list[int]], list[int]]:
    with open(filename, "r") as f:
        lines = f.readlines()
    
    freshIDRanges = []
    availableIDs = []
    for line in lines:
        line = line.strip()
        if len(line) < 1: continue
        if "-" in line:
            i,f = line.split("-")
            freshIDRanges.append([int(i), int(f)])
        else:
            availableIDs.append(int(line)) 
    
    availableIDs = list(set(availableIDs)) #make sure there is no duplication

    return (freshIDRanges, availableIDs)

def isFresh(freshIDRanges: list[list[int]], id: int) -> bool:
    for rang in freshIDRanges:
        ri, rf = rang
        if ri <= id and id <= rf:
            return True
    return False

def solution(tupleIDs: tuple[list[list[int]], list[int]]) -> int:
    freshIDRanges, availableIDs = tupleIDs
    freshIDs = []
    for id in availableIDs:
        if isFresh(freshIDRanges, id):
            freshIDs.append(id)

    print(freshIDs)
    return len(freshIDs)


if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test: ", solution(test))

    final = getInput("input.txt")
    print("Solution final: ", solution(final))