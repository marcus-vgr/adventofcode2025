def getInput(filename: str) -> list[list[int]]:
    with open(filename, "r") as f:
        lines = [line.strip().split(",") for line in f.readlines()]
        lines = [[int(l) for l in line] for line in lines]
    
    return lines

def solution(redLights: list[list[int]]) -> int:

    N = len(redLights)
    maxArea = -1
    for i in range(N-1):
        for j in range(i+1, N):
            r1, r2 = redLights[i], redLights[j]
            area = (abs(r1[0] - r2[0]) + 1) * (abs(r1[1] - r2[1]) + 1)
            maxArea = max(maxArea, area)
    
    return maxArea



if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test: ", solution(test))

    final = getInput("input.txt")
    print("Solution final: ", solution(final))