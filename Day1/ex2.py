def getInput(filename: str) -> list[str]:
    with open(filename, "r") as f:
        o = [l.strip() for l in f.readlines()]
    return o

def solution(rotations: list[str], debug: bool = False) -> int:
    
    position = 50
    nZeros = 0
    wasIn0 = 0
    for rotation in rotations:
        side = rotation[0]
        step = int(rotation[1:])
        if side == "L":
            position = (position - step)
        elif side == "R":
            position = (position + step)
        else:
            print("Error in", rotation)

        if position > 0 and position < 100:
            ... # didnt pass on zero
        elif position == 0 or position == 100:
            nZeros += 1 # just stopped on zero
        elif position > 100:
            nZeros += position // 100
        elif position < 0:
            nZeros += abs(position) // 100 + 1
            if position + step == 0: # Was in zero before, so one "rotation" doesnt count
                nZeros -= 1
        
        if debug:
            print(rotation, position, position % 100, nZeros)
        
        position = position % 100
         
    return nZeros

if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test: ", solution(test, debug=True))

    final = getInput("input.txt")
    print("Solution final: ", solution(final))