def getInput(filename: str) -> list[list[str]]:
    with open(filename, "r") as f:
        return [[c for c in l.strip()] for l in f.readlines()]
    
def printGrid(grid: list[str]):
    print( "\n".join(["".join(line) for line in grid] ))

def redo_grid(grid: list[str], toRemove: list[tuple]) -> list[list[str]]:
    for coords in toRemove:
        y,x = coords
        grid[y][x] = "."
    return grid

def solveGrid(grid: list[str]) -> list[tuple]:

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

    return positions

def solution(grid: list[str]) -> int:

    removedPapers = []

    while(True):
        #printGrid(grid)
        removedPapersLoop = solveGrid(grid)
        if len(removedPapersLoop) < 1:
            break
        grid = redo_grid(grid, removedPapersLoop)
        removedPapers = removedPapers + removedPapersLoop

    return len(removedPapers)


if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test: ", solution(test))

    final = getInput("input.txt")
    print("Solution final: ", solution(final))