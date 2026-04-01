class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []
        

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(val)
            self.minSt.append(val)
            return

        if val < self.minSt[-1]:
            self.st.append(val)
            self.minSt.append(val)
        else:
            self.st.append(val)
            self.minSt.append(self.minSt[-1])

    def pop(self) -> None:
        self.st.pop()
        self.minSt.pop()

    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        return self.minSt[-1]
    
