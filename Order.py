import sys
import time

class Menu:
    def __init__(self):
        self.dtype = ""
        self.next = None
        self.root = None
        
class Dish:
    def __init__(self):
        self.name = ''
        self.price = 0
        self.rlink = None
        self.llink = None
        self.ID = 0


class Order:
    def __init__(self):
        self.mhead = Menu()
        
    def build_menu(self):
        
        try:
            inputStream = open('Menu.dat','r')
        except FileNotFoundError:
            print('Not Found File')
            sys.exit(1)
        
        dish = inputStream.readline().strip().split(' ')
        ptr = None
        ID = 1
        while dish[0]:
            if dish[len(dish)-1]=="0":
                m = Menu()
                name = ""
                for i in dish:
                    if not i.isdigit():
                        name = name+i+" "
                m.dtype = name
                ptr = self.mhead
                while ptr.next:
                    print(ptr.dtype)
                    ptr = ptr.next
                ptr.next = m
                ptr = ptr.next
            else:
                name = ""
                price = 0
                
                for i in dish:
                    if i.isdigit():
                        price = int(i)
                    else:
                        name = name+i+" "
                self.add_dish(ID,name,price,ptr)
                ID+=1
            dish = inputStream.readline().strip().split(' ')
        print("import menu finish")
        inputStream.close()
                        
    def add_dish(self,ID,name,price,menu):
        prev = None
        node = None
        ptr = Dish()
        ptr.ID = ID
        ptr.name = name
        ptr.price = price
        if menu.root==None:
            menu.root = ptr
        else:
            node = menu.root
            while node!=None:
                prev = node
                if ptr.price < node.price:
                    node = node.llink
                else:
                    node = node.rlink
            if ptr.price < prev.price:
                prev.llink = ptr
            else:
                prev.rlink = ptr
    
    def show_menu(self):
        mptr = self.mhead.next
        while mptr:
            print(mptr.dtype+":")
            self.inorder(mptr.root)
            mptr = mptr.next
    
    def inorder(self,node):
        if node!=None:
            self.inorder(node.llink)
            print("%d. %-25s | %d" %(node.ID,node.name,node.price))
            self.inorder(node.rlink)      
    
    def search(self,ID):
        mptr = self.mhead.next
        while mptr:
            node = mptr.root
            while node!= None:
                if ID==node.ID:
                    return node
                elif ID<node.ID:
                    node = node.llink
                else:
                    node = node.rlink
            mptr = mptr.next
        return None
        
