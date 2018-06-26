# CodeSkulptor runs Python programs in your browser.
class myStack:
    items = []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()
    def peek(self):
        if (len(self.items)) == 0:
            return None
        return self.items[-1]
    def isEmpty(self):
        return len(self.items) == 0
    def isFull(self):
        return len(self.items) == 2
    def printStack(self):
        print self.items
    
class SetofStacks:
    stackSet = []

    def SetofStacks(self):
        temp_Stack = myStack()
        self.stackSet.append(temp_Stack)

    def pop(self):
        if(len(self.stackSet) > 0):
            currStack = self.stackSet[-1]
        else:
            print("Empty Set of Stacks")
            return

        currStack.pop()
        if (currStack.isEmpty()):
            self.stackSet.pop()


    def push(self,input_data):
        if (len(self.stackSet) == 0):
            temp_Stack = myStack()
            self.stackSet.append(temp_Stack)           

        currStack = self.stackSet[-1]

        if(currStack.isFull()):
            temp_Stack = myStack()
            self.stackSet.append(temp_Stack)
            currStack = self.stackSet[-1]

        currStack.push(input_data)

    def printSet(self):
        for temp in self.stackSet:
            temp.printStack()

    def popAt(self,index):
        if(index>= 0 and index < len(self.stackSet)):

            currStack = self.stackSet[index]
            if(currStack.isEmpty()):
                print("Requested Stack is empty")
            else:
                currStack.pop()
                if (currStack.isEmpty()):
                    self.stackSet.pop(index)
        else:
            print("Wrong index entered")
            return

ss = SetofStacks()

ss.push(1)
ss.push(2)
ss.push(3)
ss.push(4)
ss.push(5)
ss.push(6)
ss.push(7)
ss.push(8)
ss.push(9)
ss.push(10)

ss.printSet()
 

ss.popAt(5)
#Wrong index entered

ss.popAt(1)
ss.popAt(1)
ss.popAt(1)

ss.printSet()
# http://www.codeskulptor.org/#user44_wIqSNCRcTX_6.py
# http://www.codeskulptor.org/#user44_zJWcL9n5E2_1.py
