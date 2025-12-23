def getInput(filename: str) -> tuple[list[list[int]], list[str]]:
    with open(filename, "r") as f:
        lines = f.readlines()
    
    idxsOperations, operations = [], []
    lastLine = lines[-1]
    for i,char in enumerate(lastLine):
        if char in ["*","+"]:
            operations.append(char)
            idxsOperations.append(i)
    idxsOperations.append(len(lastLine))

    numbers = []
    for i in range(len(idxsOperations)-1):
        tmp = []
        for j in range(len(lines)-1):
            tmp.append(lines[j][idxsOperations[i]:idxsOperations[i+1] -1*(i != len(idxsOperations)-2)])
        numbers.append(tmp)

    chepalopodNumbers = []
    for col in numbers:
        nDigits = len(col[0])
        maxPower = len(col)
        tmp = []
        for digit in range(nDigits):
            number = ""
            for pow in range(maxPower):
                number += col[pow][digit]
            tmp.append(int(number.strip()))
        chepalopodNumbers.append(tmp)

    return (chepalopodNumbers, operations)


def sumList(l: list[str]) -> int:
    return sum(l)

def prodList(l: list[str]) -> int:
    prod = 1
    for n in l:
        prod = prod * n
    return prod 

def solution(numbersList: list[list[int]], operations: list[str]) -> int:

    results = []

    for i in range(len(numbersList)):
        op = operations[i]
        if op == "+":
            result = sumList(numbersList[i])
        elif op == "*":
            result = prodList(numbersList[i])
        else:
            raise ValueError(f"{op} not supported!")
        results.append(result)

    print(results)
    return sumList(results)

if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test: ", solution(*test))

    final = getInput("input.txt")
    print("Solution final: ", solution(*final))