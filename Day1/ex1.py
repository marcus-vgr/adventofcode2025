def getInput(filename: str) -> list[str]:
    with open(filename, "r") as f:
        o = [l.strip() for l in f.readlines()]
    return o

def solution(rotations: list[str]) -> int:
    
    position = 50
    nZeros = 0
    for rotation in rotations:
        side = rotation[0]
        step = int(rotation[1:])
        if side == "L":
            position = (position - step) % 100
        elif side == "R":
            position = (position + step) % 100
        else:
            print("Error in", rotation)
        if position == 0:
            nZeros += 1
    
    return nZeros

if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test: ", solution(test))

    final = getInput("input.txt")
    print("Solution final: ", solution(final))