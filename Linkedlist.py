class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class LinkedList:
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
        print("\t[___The Linked List___]")
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

    def sort(self,reverse=False):
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
                if (f.val > s.val) if reverse else (f.val < s.val):
                    t.next=f
                    f=f.next
                else:
                    t.next=s
                    s=s.next
                t=t.next

            t.next = s if s else f
            return dummy.next

        self.head=divide(self.head)

    def deleteAtEnd(self,n=1):
        cnt = self.length(False)
        if cnt==0:
            raise("List Is Empty!!!")
        n=cnt-n
        dummy = t = Node(0,self.head)
        while n>0 and t.next:
            t = t.next
            n-=1
        t.next = None
        self.head=dummy.next

    def deleteAtBegining(self,n=1):
        if not self.head :
            raise("List Is Empty!!!")
        while n!=0 and self.head:
            self.head = self.head.next
            n-=1

    def deleteAt(self,pos):
        if self.head and pos==1:
            self.head=self.head.next
            return 
        t = self.head
        cnt = 2
        while t.next:
            if cnt==pos:
                t.next=t.next.next
                return
            cnt+=1
            t = t.next
        raise("Invalid Position For Delete")

    def reverse(self):
        if not self.head or not self.head : return 

        tem = self.head
        pre = None
        while tem.next:
            nxt = tem.next
            tem.next = pre
            pre = tem
            tem = nxt
        self.head = tem
        tem.next = pre

    def bulkInsertAtStart(self,ar):
        dummy = t = Node(0)
        for ele in ar:
            t.next = Node(ele)
            t = t.next
        t.next = self.head
        self.head = dummy.next
    def bulkInsertAtEnd(self,ar):
        dummy = t = Node(0)
        for ele in ar:
            t.next = Node(ele)
            t = t.next
        t = self.head
        if self.head :
            while t.next:
                t = t.next
            t.next = dummy.next
        else:
            self.head = dummy.next

    def length(self,s=True):
        t = self.head
        cnt = 0
        while t:
            cnt+=1
            t = t.next
        if s :print(f"The length of the list --> {cnt}")
        return cnt
    def reset(self):
        self.head=None


class CLI_Linked_List :
    def __init__(self):
        self.list = LinkedList()
    def menu(self):
        print("\n\t|----- Linked List CLI-Application -----|\n")
        print("1. InsertAtBegining\t\t8.  DeleteAtBegining")
        print("2. InsertAtEnd\t\t\t9.  DeleteAtEnd")
        print("3. InsertAtPosition\t\t10. DeleteAtPosition")
        print("4. BulkInsertAtStart\t\t11. Sort")
        print("5. BulkInsertAtEnd\t\t12. Search")
        print("6. Reverse\t\t\t13. Lenght")
        print("7. Reset\t\t\t14. Exit")
        self.list.display()
    def run(self):
        while True:
            self.menu()
            try:
                opt = int(input("Enter Your Choice: "))
                if opt==1:
                    ele = int(input("Enter value to insert at begining : "))
                    self.list.insertAtBegining(ele)
                elif opt==2:
                    ele = int(input("Enter value to insert at end : "))
                    self.list.insertAtEnd(ele)
                elif opt==3:
                    ele = int(input("Enter value to insert : "))
                    pos = int(input("Enter position to insert : "))
                    self.list.insert(ele,pos)
                elif opt==4:
                    ar = list(map(int,input("Enter values separated by space : ").split()))
                    self.list.bulkInsertAtStart(ar)
                elif opt==5:
                    ar = list(map(int,input("Enter values separated by space : ").split()))
                    self.list.bulkInsertAtEnd(ar)
                elif opt==6:
                    self.list.reverse()
                elif opt==7:
                    w = input("Are you sure to RESET (y/n):").strip().lower()=="y"
                    if w:
                        self.list.reset()
                elif opt==8:
                    n = int(input("Enter number of elements to be deleted at begining : "))
                    self.list.deleteAtBegining(n)
                elif opt==9:
                    n = int(input("Enter number of elements to be deleted at end : "))
                    self.list.deleteAtEnd(n)
                elif opt==10:
                    n = int(input("Enter position to delete element :"))
                    self.list.deleteAt(n)                    
                elif opt==11:
                    ch = input("Sort in descending order (y/n) : ").strip().lower()=="y"
                    self.list.sort(reverse = ch)
                elif opt==12:
                    ele = int(input("Enter value to Search : "))
                    self.list.search(ele)                    
                elif opt==13:
                    self.list.length()
                elif opt==14:
                    print("\tBye Bye!!!!!!!!!!!!!!!")
                    print("\t\tYou Are Exiting CLI_APPLICATION--------->>>>>>")
                    break
                else:
                    print("--------->>Invalid Option !!!!\nTry Again")

            except Exception as e:
                print(f"ERROR : {e}")




if __name__ == "__main__":
    app = CLI_Linked_List()
    app.run()




