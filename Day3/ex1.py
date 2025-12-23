def getInput(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [l.strip() for l in f.readlines()]
    
def getLargestJoltage(s: str) -> int:
    
    N = len(s)
    
    idx = 1
    IDX_I = 0
    firstDigit = s[IDX_I]
    while(idx < N-1):
        if firstDigit < s[idx]:
            firstDigit = s[idx]
            IDX_I = idx
        if firstDigit == "9": 
            break
        idx += 1

    idx = IDX_I + 2
    IDX_F = IDX_I + 1
    secondDigit = s[IDX_F]
    while(idx < N):
        if secondDigit < s[idx]:
            secondDigit = s[idx]
            IDX_F = idx
        if secondDigit == "9": 
            break
        idx += 1
    
    return int( firstDigit + secondDigit )
    

def solution(banks: list[str]) -> int:
    joltages = []
    for bank in banks:
        joltages.append(getLargestJoltage(bank))
    
    print(joltages)
    return sum(joltages)

if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test: ", solution(test))

    final = getInput("input.txt")
    print("Solution final: ", solution(final))