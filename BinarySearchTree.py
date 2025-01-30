class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self,val):
        def ins(root):
            if root.val>val :
                if root.left:
                    ins(root.left)
                else:
                    root.left = Node(val)
            else:
                if root.right:
                    ins(root.right)
                else:
                    root.right = Node(val)

        if not self.root:
            self.root = Node(val)
        else:
            ins(self.root)

    def traverse(self,order="in",dis=True):
        def inorder(root):
            if not root:return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        def preorder(root):
            if not root:return 
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        def postorder(root):
            if not root:return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        def levelorder(root):
            res.append([root.val])
            q = [root]
            while q!=[]:
                n = len(q)
                level = list()
                for i in range(n):
                    cur = q.pop(0)
                    if cur.left:
                        q.append(cur.left)
                        level.append(cur.left.val)
                    else:
                        level.append(None)
                    if cur.right:
                        q.append(cur.right)
                        level.append(cur.right.val)
                    else:
                        level.append(None)
                res.append(list(level)) 

        if not self.root:
            print("(Tree Empty)!!!")
            return []
        res = []
        if order=='in': inorder(self.root)
        elif order=='pre': preorder(self.root)
        elif order=="post": postorder(self.root)
        else:
            levelorder(self.root)            
            res=res[:-1]

        if order=="level" and dis:
            print("\t__Level Order Traversal__")
            for i,level in enumerate(res):
                print(f" Level-{i+1} --> {level}")
            print()
        elif dis:
            print(f"\t__{order.capitalize()}order traversal__\n  {res}\n")
        else:
            return res

    def treeHeight(self,disp=True):
        def h(root):
            if not root: return 0
            return 1+max(h(root.left),h(root.right))
        height = h(self.root)
        if disp:print(f"Height of Tree - {height}")
        return height

    def display(self):
        def p(node, prefix="", is_left=True):
            if not node:
                return
            if node.right:
                p(node.right, prefix + ("│    " if is_left else "     "), False)

            print(prefix + ("└── " if is_left else "┌── ") +"["+str(node.val)+"]")
        
            if node.left:
                p(node.left, prefix + ("     " if is_left else "│    "), True)

        if not self.root:
            print("(empty tree)\n")
            return
        
        p(self.root)
        print()
        
    def reset(self):
        self.root = None

    def search(self,key):
        def f(root):
            if not root:return False
            elif root.val==key:return True
            return (root.left and f(root.left)) or (root.right and f(root.right))

        tem ="" if f(self.root) else "not "
        print(f"__ Value-{key} {tem}present in the tree __")

    def min(self,root=None):
        root = self.root if root==None else root
        if not root:
            return 
        while root.left:
            root = root.left
        return root

    def max(self,root=None):
        root = self.root if root==None else root
        if not root:
            return
        while root.right:
            root=root.right
        return root

    def delete(self,key):
        def dele(root,key):
            if not root : return root

            elif root.val>key :
                root.left=dele(root.left,key)
            elif root.val<key:
                root.right=dele(root.right,key)
            else:
                if not root.right and not root.left : return None
                elif root.left==None : return root.right
                elif root.right==None : return root.left
                else:
                    tem = self.min(root.right)
                    root.val=tem.val
                    root.right = dele(root.right,root.val)
            return root
        if isinstance(key,int):
            self.root = dele(self.root,key)
        else:
            for ele in key:
                self.root = dele(self.root,ele)

        
class CLI_BST:
    def __init__(self):
        self.tree = BST()
    def menu(self):
        print("\n\t|----- BST CLI-Application -----|\n")
        print("1. Insert\t6. Height")
        print("2. BulkInsert\t7. Search")
        print("3. Traverse\t8. Find Min&Max values")
        print("4. Delete\t9. BulkDelete")
        print("5. Reset\t10. Exit\n")
        self.tree.display()
    def run(self):
        while True:
            self.menu()
            try:
                opt = int(input("Enter Your Choice: "))
                if opt==1:
                    ele = int(input("Enter value to insert : "))
                    self.tree.insert(ele)
                elif opt==2:
                    ar = list(map(int,input("Enter values separated by space : ").split()))
                    for ele in ar:
                        self.tree.insert(ele)
                elif opt==3:
                    print("\tTypes of Traversal")
                    print("1-PreOrder   2-InOrder   3-PostOrder   4-LevelOrder")
                    ch = int(input("Enter choice of traversal: "))
                    di = {1:"pre",2:"in",3:"post",4:"level"}
                    self.tree.traverse(di.get(ch))
                elif opt==4:
                    self.tree.delete(int(input("Enter value to delete : ")))
                elif opt==5:
                    w = input("Are you sure to RESET (y/n):").strip().lower()=="y"
                    if w:
                        self.tree.reset()              
                elif opt==6:
                    self.tree.treeHeight()
                elif opt==7:
                    ele = int(input("Enter value to Search : "))
                    self.tree.search(ele)               
                elif opt==8:
                    min_ = self.tree.min()
                    if min_ :
                        max_ = self.tree.max()
                        print(f"MIN = {min_.val} & MAX = {max_.val}")
                    else:
                        print("Tree is empty!!!")
                elif opt==9:
                    self.tree.delete(list(map(int,input("Enter values to be deleted : ").split())))
                elif opt==10:
                    print("\tBye Bye!!!!!!!!!!!!!!!")
                    print("\t\tYou Are Exiting CLI_APPLICATION--------->>>>>>")
                    break
                else:
                    print("--------->>Invalid Option !!!!\nTry Again")

            except Exception as e:
                print(f"ERROR : {e}")


if __name__ == "__main__":
    app = CLI_BST()
    app.run()
                 
