def getInput(filename: str) -> tuple[list[list[int]], list[str]]:
    with open(filename, "r") as f:
        lines = f.readlines()
    print(lines)

    N = len(lines)
    numbers = []
    for i in range(N-1):
        line = lines[i].strip().split(" ")
        line = [int(l) for l in line if len(l) > 0]
        numbers.append(line)

    numbersOrdered = []
    for i in range(len(numbers[0])):
        numbersOrdered.append(
            [numbers[j][i] for j in range(len(numbers))]
        )

    operations = lines[-1].strip().split(" ")
    operations = [l for l in operations if len(l) > 0]
    
    return (numbersOrdered, operations)

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