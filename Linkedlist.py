class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class LinkedList:
    head = None
    def __init__(self,val=0):
        self.head = None
    def insertAtEnd(self,val):
        if self.head :
            t = self.head
            while t.next:
                t=t.next
            t.next = Node(val)
        else:
            self.head=Node(val)
    def insertAtBegining(self,val):
        t = Node(val,self.head)
        self.head = t
    def insert(self,val,pos=1):
        if pos<=0:
            raise("Not a valid postion!!!")
        if not self.head or pos==1:
            self.head = Node(val,self.head)
        else:
            cnt = 1 
            t = self.head
            while t.next and cnt!=pos-1:
                cnt+=1
                t = t.next
            t.next = Node(val,t.next)

    def display(self):
        print("\t|-----The Linked List -----|")
        if self.head:
            t = self.head
            while t.next:
                print(f'[{t.val}]-->',end="")
                t=t.next
            print(f'[{t.val}]')
        else :
            print("None!!!!!")
        print()
    def search(self,key=None):
        if not key:raise("No Search key has passed")
        t = self.head
        cnt = 1
        while t:
            if key==t.val:
                print(f"Element-{key} found at postition {cnt}\n")
                return 
            cnt+=1
            t = t.next
        print(f"Element-{key} not present in List!!!!\n")

    def sort(self):
        def divide(root):
            if not root or not root.next :
                return root

            fast = slow = root
            pre=None
            while fast and fast.next :
                pre=slow
                slow=slow.next
                fast=fast.next.next
            mid = slow
            pre.next=None

            root = divide(root)
            mid = divide(mid)
            return merge(root,mid)

        def merge(f,s):
            dummy = t = Node(0)
            while f and s:
                if f.val < s.val :
                    t.next=f
                    f=f.next
                else:
                    t.next=s
                    s=s.next
                t=t.next

            t.next = s if s else f
            return dummy.next



        self.head=divide(self.head)





l = LinkedList()
l.insert(10,6)
l.insert(1,1)
l.insert(11,2)
l.insert(9,1)
l.insertAtEnd(10)
l.insert(1,1)
l.display()
l.search(10)
l.insertAtBegining(9)
l.insert(11)
l.insertAtEnd(11)
l.display()
l.search(100)
l.sort()
l.display()
l.insert(1000,1)
l.display()
l.sort()
l.display()


