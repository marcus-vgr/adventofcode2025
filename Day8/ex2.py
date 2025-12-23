def getInput(filename: str) -> list[list[int]]:
    with open(filename, "r") as f:
        lines = [line.strip().split(",") for line in f.readlines()]
        lines = [ [int(l) for l in line] for line in lines ]
    return lines

def distance(v1: list[int], v2: list[int]) -> float:
    return ( (v1[0] - v2[0])**2 + (v1[1] - v2[1])**2 + (v1[2] - v2[2])**2 )**0.5

def createDistanceVector(boxes: list[list[int]]) -> list[tuple]:

    distanceVector = []
    N = len(boxes)
    for i in range(N-1):
        for j in range(i+1,N):
            dist = distance(boxes[i], boxes[j])
            distanceVector.append((i,j,dist))

    distanceVector = sorted(distanceVector, key = lambda x: x[-1])

    return distanceVector

def solution(boxes: list[list[int]]) -> int:

    result = -1

    distanceVector = createDistanceVector(boxes)
    DUMMY_ID = -1
    box_circuit_id = [DUMMY_ID] * len(boxes)
    circuitNumber = 0
    for pair in distanceVector:
        b1, b2 = pair[0], pair[1]
        if box_circuit_id[b1] == DUMMY_ID and box_circuit_id[b2] == DUMMY_ID: # Forming a new circuit
            box_circuit_id[b1] = circuitNumber
            box_circuit_id[b2] = circuitNumber
            circuitNumber += 1
        elif box_circuit_id[b1] != DUMMY_ID and box_circuit_id[b2] == DUMMY_ID: # Merging b2 to b1 circuit
            box_circuit_id[b2] = box_circuit_id[b1]
        elif box_circuit_id[b1] == DUMMY_ID and box_circuit_id[b2] != DUMMY_ID: # Merging b1 to b2 circuit
            box_circuit_id[b1] = box_circuit_id[b2]
        else: # merging two different circuits
            id_b1 = box_circuit_id[b1]
            id_b2 = box_circuit_id[b2]
            for i in range(len(boxes)):
                if box_circuit_id[i] == id_b2:
                    box_circuit_id[i] = id_b1

        if len(set(box_circuit_id)) == 1: ## they are all joined
            print(pair)
            result = boxes[b1][0] * boxes[b2][0]
            break

    return result


if __name__ == "__main__":

    test = getInput("test.txt")
    print("Solution test", solution(test))

    final = getInput("input.txt")
    print("Solution final", solution(final))