from collections import deque

class Day10:

    def __init__(self, filename: str):
        self.readInput(filename)

    def readInput(self, filename: str):

        with open(filename, "r") as f:
            lines = f.readlines()

        self.diagrams = []
        self.commands = []
        self.joltages = []
        for line in lines:
            line = line.strip().split()
            diagram = [int(elem) for elem in line[0].replace("[","").replace("]","").replace(".","0").replace("#","1")]
            command = [eval(cmd.replace(")",",)")) for cmd in line[1:-1]]
            joltage = [int(elem) for elem in line[-1].replace("{","").replace("}","").split(",")]
            self.diagrams.append(diagram)
            self.commands.append(command)
            self.joltages.append(joltage)
    
    def solveMachine(self, diagram: list[int], commands: list[tuple]) -> int:
        
        N = len(diagram)
        start = [0] * N # all are off
        queue = deque([start])
        stateDict = {tuple(start): 0}        

        while len(queue) > 0:
            state = queue.popleft()
            if state == diagram:
                return stateDict[tuple(state)]
            
            for cmd in commands:
                newstate = state.copy()
                for n in cmd:
                    newstate[n] = 0 if newstate[n] == 1 else 1 
                if tuple(newstate) not in stateDict:
                    stateDict[tuple(newstate)] = stateDict[tuple(state)] + 1
                    queue.append(newstate)

        return -1


    def solution(self) -> int:

        nPresses = []
        for diagram, commands in zip(self.diagrams, self.commands):
            nPresses.append(
                self.solveMachine(diagram, commands)
            )

        return sum(nPresses)


    
if __name__ == "__main__":

    test = Day10("test.txt")
    print("Solution test ex1: ", test.solution())
    
    final = Day10("input.txt")
    print("Solution final ex1: ", final.solution())
    
