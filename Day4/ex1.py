def getInput(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [l.strip() for l in f.readlines()]
    

def solution(grid: list[str]) -> int:

    Y = len(grid)
    X = len(grid[0])
    positions = []

    for y in range(Y):
        for x in range(X):
            if grid[y][x] != "@": continue

            nPapersAdjacent = 0
            adjacentPositions = [
                (y-1,x-1), (y-1,x), (y-1,x+1),
                (y,x-1), (y,x+1),
                (y+1,x-1), (y+1,x), (y+1,x+1),
            ]
            for coordinates in adjacentPositions:
                adjY, adjX = coordinates
                if adjY < 0 or adjY >= Y or adjX < 0 or adjX >= X:
                    continue
                if grid[adjY][adjX] == "@":
                    nPapersAdjacent += 1
            
            if nPapersAdjacent < 4:
                positions.append((y,x)) 

    #print(positions)

    return len(positions)


if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test: ", solution(test))

    final = getInput("input.txt")
    print("Solution final: ", solution(final))