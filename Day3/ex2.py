def getInput(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [l.strip() for l in f.readlines()]
    
def getLargestJoltage(s: str, nDigits: int = 12) -> int:
    
    N = len(s)
    digits = []

    idx = 0
    IDX_D = -1
    nDigitsLeft = nDigits
    while(nDigitsLeft > 0):
        digitCandidate = "-1"

        while(idx <= N-nDigitsLeft):
            if digitCandidate < s[idx]:
                digitCandidate = s[idx]
                IDX_D = idx
            if digitCandidate == "9": 
                break
            idx += 1
        
        digits.append(digitCandidate)
        idx = IDX_D + 1
        nDigitsLeft -= 1    

    return int( "".join(digits) )
    

def solution(banks: list[str], nDigits: int = 12) -> int:
    joltages = []
    for bank in banks:
        joltages.append(getLargestJoltage(bank,nDigits))
    
    print(joltages)
    return sum(joltages)

if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test: ", solution(test))

    final = getInput("input.txt")
    print("Solution final: ", solution(final))