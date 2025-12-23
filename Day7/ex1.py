def getInput(filename: str) -> list[list[str]]:
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f.readlines()]
    

def printManifold(manifold: list[list[str]]):
    toPrint = "\n".join( ["".join(line) for line in manifold]    )
    print(toPrint, "\n")

def passBoundaries(xi: int, yi: int, Xmax: int, Ymax: int) -> bool:
    if xi < 0 or yi < 0 or xi > Xmax-1 or yi > Ymax-1:
        return False
    return True

def solution(manifold: list[list[str]]) -> int:

    Xmax = len(manifold[0])
    Ymax = len(manifold)

    nSplits = 0

    yi = 0
    for i,char in enumerate(manifold[yi]):
        if char == "S":
            xi = i
    beams_coords = set([(xi,yi)])
    for y in range(1, Ymax):
        new_beams_coords = set()
        for coord in beams_coords:
            xi = coord[0]
            yi = coord[1] + 1
            if manifold[yi][xi] == ".":
                new_beams_coords.add((xi,yi))
                manifold[yi][xi] = "|"
            elif manifold[yi][xi] == "^":
                nSplits += 1
                if( passBoundaries(xi-1,yi,Xmax,Ymax) ):
                    new_beams_coords.add((xi-1,yi))
                    manifold[yi][xi-1] = "|"
                if( passBoundaries(xi+1,yi,Xmax,Ymax) ):
                    new_beams_coords.add((xi+1,yi))
                    manifold[yi][xi+1] = "|"
    
        beams_coords = new_beams_coords
        #printManifold(manifold)
    
    return nSplits


if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test: ", solution(test))

    final = getInput("input.txt")
    print("Solution final: ", solution(final))