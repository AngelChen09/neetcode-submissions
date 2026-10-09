class LinkedList:
    
    def __init__(self):
        self.llist = []

    def get(self, index: int) -> int:
        if (index < len(self.llist)):
            return self.llist[index]
        return -1

    def insertHead(self, val: int) -> None:
        self.llist.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.llist.append(val)

    def remove(self, index: int) -> bool:
        if (index < len(self.llist)):
            self.llist = self.llist[:index] + self.llist[(index + 1):]
            return True
        return False

    def getValues(self) -> List[int]:
        return self.llist
        
