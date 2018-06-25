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
    def remove_dups_no_buffer(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        curr = head
        print curr.data, curr.next
        while curr.next != None:
            runner = curr
            while runner.next:
                if runner.next.data == curr.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            curr = curr.next
        return head
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head)
#head = mylist.remove_dups_2_1(head)
head = mylist.remove_dups_no_buffer(head)
mylist.display(head)
#http://www.codeskulptor.org/#user44_YntoPFkZzm_13.py
