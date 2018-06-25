class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next
        print ' '
    def insert(self,head,data): 
        if head == None:
            head = Node(data)
        else:
            current = head
            while current.next:
                current = current.next
            current.next = Node(data)
        return head
    def remove_dups_2_1(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        current = head
        seen = set([current.data])
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next
        return head
    
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head)
head = mylist.remove_dups_2_1(head)
mylist.display(head)
