import sys
import delivery_time
import chainstore

class Customer:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.password = 0
        self.point = 0
        self.bf = 0
        self.llink = None
        self.rlink = None

class Order:
    def __init__(self):
        self.meal = None
        self.next = None
        self.total = 0
        self.desk_number = 0
        
class Meal:
    def __init__(self):
        self.next = None
        self.ID = 0
        self.name = ''
        self.desk = 0
        self.price = 0
        self.number = 0

root = None
ptr = None
current = None
prev = None
pivot = None
pivot_prev = None
nodecount = 0

def insert_f():
    global nodecount
    print('\n=====ADD CUSTOMER=====')
    id = eval(input('Enter customer id: '))
    name = input('Enter customer name: ')
    point = eval(input('Enter customer point: '))
    nodecount+=1
    access(id,name,point,0) #員工手動新增會員 密碼將預設為0

def access(id,name,point,password):
    global ptr
    global root
    global current
    global prev
    global pivot

    op = 0
    current = root

    while current != None and id != current.id:
        if id < current.id:
            prev = current
            current = current.llink

        else:
            prev = current
            current = current.rlink

    if current == None or id != current.id:
        ptr = Customer()
        ptr.id = id
        ptr.name = name
        ptr.point = point
        ptr.password = password
        ptr.llink = None
        ptr.rlink = None
        if root == None:
            root = ptr
        elif ptr.id < prev.id:
            prev.llink = ptr
        else:
            prev.rlink = ptr
        bf_count(root)
        pivot = pivot_find()
        if pivot != None:
            op = type_find()
            if op == 11:
                type_ll()
            elif op == 22:
                type_rr()
            elif op == 12:
                type_lr()
            elif op == 21:
                type_rl()
        bf_count(root)
    else:
        print('Customer %d has existed'%id)


def bf_count(trees):
    if trees != None:
        bf_count(trees.llink)
        bf_count(trees.rlink)
            
        trees.bf = height_count(trees.llink) - height_count(trees.rlink)

def height_count(trees):
    if trees == None:
        return 0
    elif trees.llink == None and trees.rlink == None:
        return 1
    elif height_count(trees.llink) > height_count(trees.rlink):
        return 1+height_count(trees.llink)
    else:
        return 1 + height_count(trees.rlink)

def pivot_find(): 
    global root
    global pivot_prev
    global current
    global prev
    global pivot
    global nodecount

    current = root
    prev = None
    for i in range(nodecount):
        if current.bf < -1 or current.bf > 1:
            pivot = current
            if pivot != root:
                pivot_prev = prev
        if current.bf >0:
            prev = current
            current = current.llink
        elif current.bf < 0 :
            prev = current
            current = current.rlink
    return pivot

def type_find():
    global current
    global pivot
    op_r = 0
    current = pivot
    for i in range(2):
        if current.bf > 0:
            current = current.llink
            if op_r == 0:
                op_r += 10
            else:
                op_r += 1  
        elif current.bf <0:
            current = current.rlink
            if op_r == 0:
                op_r += 20
            else:
                op_r += 2

    return op_r

def type_ll():
    global root
    global pivot
    global pivot_prev

    pivot_next = pivot.llink
    temp = pivot_next.rlink
        
    pivot_next.rlink = pivot
    pivot.llink = temp
        
    if pivot == root:
        root = pivot_next
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = pivot_next
    else:
        pivot_prev.rlink = pivot_next

def type_rr():
    global root
    global pivot
    global pivot_prev

    pivot_next = pivot.rlink
    temp = pivot_next.llink
        
    pivot_next.llink = pivot
    pivot.rlink = temp
        
    if pivot == root:
        root = pivot_next
    elif pivot_prev.rlink == pivot:
        pivot_prev.rlink = pivot_next
    else:
        pivot_prev.llink = pivot_next
            

def type_lr():
    global root
    global pivot
    global pivot_prev

    pivot_next = pivot.llink
    temp = pivot_next.rlink
        
    pivot.llink = temp.rlink
    pivot_next.rlink = temp.llink
        
    temp.llink = pivot_next
    temp.rlink = pivot
   
    if pivot == root:
        root = temp
    elif pivot_prev.llink == pivot:
            pivot_prev.llink = temp
    else:
        pivot_prev.rlink = temp

def type_rl():
    global root
    global pivot
    global pivot_prev
    pivot_next = pivot.rlink
    temp = pivot_next.llink
        
    pivot.rlink = temp.llink
    pivot_next.llink = temp.rlink
        
    temp.rlink = pivot_next
    temp.llink = pivot
        
    if pivot == root:
        root = temp
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = temp
    else:
        pivot_prev.rlink = temp

def list_f():
    global root
    if root == None:
        print('No customer record existed')
    else:
        list_cus()

def list_cus():
    global root
    print('\n%-10s %-15s %-3s'%('ID','Name','Point'))
    #以中序法輸出資料
    inorder(root)

def inorder(node):
    if node != None:
        inorder(node.llink)
        print('%-10s %-15s %-3s'%(str(node.id), node.name, str(node.point)))
        inorder(node.rlink)


def modify_f():
    global root
    global current

    if root == None:
        print('No customer record!')
        return 
    else:
        print('DEDUCT POINT')
        id = eval(input('Enter customer id: '))

        current = root
        while current != None and id != current.id:
            if id < current.id:
                current = current.llink
            else:
                current = current.rlink

        if current != None:
            print('customer id: ',current.id )
            print('customer name: ',current.name)
            print('customer point: ',current.point)

            point = eval(input('Enter point to deduct: '))
            if current.point < point:
                print("point is not enough")
                return
            else:
                current.point -= point
                print('customer %d is deducted %d, remain %d'%(id,point,current.point))
        else:
            print('\nCustomer %d not found'%id)

def del_member():
    global root
    global current
    global prev
    global pivot
    global nodecount

    clear = None
    if root == None:
        print('\n No cutomer record !')
    else:
        print('\n=====DELETE CUSTOMER=====')
        id = eval(input('Enter customer id:'))
        tempn = id #find delete node
        current = root

        while current != None and id != current.id:
            if id < current.id:
                prev = current
                current = current.llink
            else:
                prev = current
                current = current.rlink

        if current != None and id == current.id: #底下無左右子樹
            if current.llink == None and current.rlink == None:
                clear = current
                if id == root.id: #欲刪除資料為root
                    root = None
                else: #不為root 便是左子樹或右子樹
                    if id < prev.id:
                        prev.llink = None
                    else:
                        prev.rlink = None
                clear = None
            else:
                if current.llink != None:
                    clear = current.llink
                    while clear.rlink != None:
                        prev = clear
                        clear = clear.rlink
                    current.id = clear.id
                    current.name = clear.name
                    current.point = clear.point
                    if current.llink == clear:
                        current.llink = clear.llink
                    else:
                        prev.rlink = clear.llink
                else:
                    clear = current.rlink
                    while clear.llink != None:
                        prev= clear
                        clear = clear.llink
                    current.id = clear.id
                    current.name = clear.name
                    current.point = clear.point
                    if current.rlink == clear:
                        current.rlink = clear.rlink
                    else:
                        prev.llink = clear.rlink  
                clear = None
            bf_count(root)
            if root != None:
                pivot = pivot_find()
                while pivot != None:
                    op = type_find()
                    if op == 11:
                        type_ll()
                    elif op == 22:
                        type_rr()
                    elif op == 12:
                        type_lr()
                    elif op == 21:
                        type_rl()
                    bf_count(root)
                    pivot = pivot_find()
            nodecount-=1
            print('Customer %d has been delete'%id)
        else:
            print('Customer %d not found'%id)                  


def background_operation():
    while True:
        print("\n************ Background Operation ************")
        print("<1>Add member")
        print("<2>delete member")
        print("<3>back")
        print("**********************************************")
        try:
            option = int(input("   Choice ： "))
        except ValueError:
            print("Not a correct number.")
            print("try again\n")

        print()
        if option == 1:
            insert_f()
        elif option ==2:
            del_member()  
        elif option == 3:
            break
        else:
            print("不正確的選項")     

def data_input():
    f = open('member.txt','r')
    while True:
        id = f.readline().strip()
        name = f.readline().strip()
        point = f.readline().strip()
        password =f.readline().strip()
        if id != '' and name != '' and point != '':
            access(int(id),name,int(point),int(password))
                 
        if f.readline() == '':
            f.close()
            print("data reading.....")
            return

def data_output():
    global root
    
    f = open('member.txt','w')
    node_queue = [root]
    while not node_queue.count(None) == len(node_queue):
        node = node_queue.pop(0)
        if node:
            f.write(str(node.id)+'\n')
            f.write(node.name+'\n')
            f.write(str(node.point)+'\n')
            f.write(str(node.password)+'\n')
            f.write('\n')
            #print(node.id,node.name,node.point, end=" ") #check
            print()
            node_queue.append(node.llink)
            node_queue.append(node.rlink)
        else:
            node_queue.append(None)
            node_queue.append(None)

    print("\n")
    print('Data writting.....')

######################## Order part #########################
def calculate_deliver_time(): #
    delivery_time.main()


ohead = Order()
ohead.next = ohead
#使用環狀鏈結
def add_orl(desk,total,meals):
    global ohead
    ptr = Order()
    ptr.next = ohead
    ptr.desk_number = desk
    ptr.total = total
    ptr.meal = meals.next
    prev = ohead
    current = ohead.next
    while current != ohead and current.desk_number >= ptr.desk_number:
        prev = current
        current = current.next
    ptr.next = current
    prev.next = ptr
    #print('Success add order')


def findnode(desk):
    global ohead
    ptr = ohead.next
    while ptr!= ohead and ptr.desk_number != desk:
        if ptr.desk_number != desk:
            ptr = ptr.next
    if ptr.total == 0:
        return None
    return ptr

def show_order():
    global ohead
    count = 0
    prev = ohead
    current = ohead.next
    if ohead.next == ohead:
        print('no order record')
    else:
        print()
        print('='*40)
        current = ohead.next
        while current != ohead:
            print('Desk:',current.desk_number,',Total dollars:',int(current.total))
            print('%-25s %-10s'%('Meal','Number'))
            find_desk_meal(current.desk_number)
            print()
            count+=1
            current = current.next

        print('='*40)
        print('There %d order(s)'%count)

def find_desk_meal(desk_number):
    global mhead
    if mhead.next == None:
        print("No meals")
        return None
    prev = mhead
    ptr = mhead.next
    while ptr != None:
        if ptr.desk == desk_number:
            print('%-25s %-10d'%(ptr.name,ptr.number))  
        prev = ptr
        ptr = ptr.next 

def delete_orl(desk_num):   
    global ohead

    if ohead.next == ohead:
        print('[所有訂單已完成 !!]')   #環狀串列已經空了
        return None
    
    else:
        prev = ohead
        current = ohead.next
    while current != ohead and desk_num != current.desk_number:
        prev = current
        current = current.next

    if current != ohead:
        prev.next = current.next
        current = None
        del_meal(desk_num)
        print("Desk %d 's order has done!"%desk_num)
    else:
        print(desk_num,'no have order')


mhead = Meal()
mhead.next = None
def add_meal(id,name,price,number,desk):
    global mhead
    ptr = Meal()
    ptr.ID = id
    ptr.name = name
    ptr.price = price
    ptr.number = number
    ptr.desk = desk
    prev = mhead
    current = mhead.next
    while current != None and current.ID >= ptr.ID:
        prev = current
        current = current.next
    ptr.next = current
    prev.next = ptr
    return ptr
def show_meals():
    global mhead
    if mhead.next == None:
        print("No meals")
        return None
    ptr = mhead.next
    print('-'*40)
    print('All meals need to do:')
    while ptr:
        print(ptr.name,'*',ptr.number)
        ptr = ptr.next 
    print('='*40)

def del_meal(desk_number):
    global mhead
    prev = mhead
    ptr = mhead.next
    if mhead.next == None:
        print("No meals")
        return None
    while ptr != None:
        if ptr.desk == desk_number:
            print(ptr.name,'*',ptr.number,'is done')
            prev.next = ptr.next
            ptr = prev
        prev = ptr
        ptr = ptr.next
                        
def nearchainstore(): 
    chainstore.main()

def Order_input(): #show all order
    global ohead
    global mhead
    f = open('order.txt','r')
    #print("start insert data")
    total = 0
    tempmeal = None
    while True:
        data = f.readline().strip()
        if len(data) == 1:
            desk = int(data)
            #print('desk:',data) 
        if len(data.split(',')) == 4:
            d =data.split(',')
            ID = int(d[0])
            name = d[1]
            price = int(d[2])
            number = int(d[3])
            meals = add_meal(ID,name,price,number,desk)
            #print('ID:',ID,'Name:',name,'Price:',price,'Number:',number)
        if data == '##':
            total = f.readline().strip().split('/')
            #print('Total:',total[0])      
            add_orl(desk,total[0],meals)
        if data == '':
            return


def Order_output():
    file = open('order.txt','w')
    global ohead
    global mhead
    if ohead.next == ohead:
        print('no order record')
    else:
        mptr = mhead.next
        current = ohead.next
        while current != ohead:
            file.write(str(current.desk_number)+'\n')
            mprev = mhead
            mptr = mhead.next
            while mptr != None:
                if mptr.desk == current.desk_number:
                    file.write(str(mptr.ID)+',')
                    file.write(mptr.name+',')
                    file.write(str(mptr.price)+',')
                    file.write(str(mptr.number))
                    file.write('\n') 
                mprev = mptr
                mptr = mptr.next 
            file.write('##')
            file.write('\n')
            file.write(str(current.total)+'/')
            file.write('\n')
            #print('Order is writting.....')
            current = current.next

################### main() #######################
def main():
    global root
    n = int(input("Enter Staff Password: "))
    if n == 123:
        data_input()
        Order_input()
        option = 0
        while True:
            print("\n********** Background Management System **********")
            print("<1>Show All Member")
            print("<2>Check Order")
            print("<3>Find Order")
            print("<4>Order is delivered !!")
            print("<5>See what meals need to do")
            print("<6>Deduct point")
            print("<7>Calculate delivery time")
            #print("<8>background operation")
            print("<8>Shortest Distance to other chainstore")
            print("<9>exit")
            print("**************************************************")

            try:
                option = int(input("   Choice ： "))
            except ValueError:
                print("Not a correct number.")
                print("try again\n")

            print()
            if option == 1:
                list_f()
            elif option ==2:
                show_order()
            elif option == 3:
                desk = eval(input('Enter desk number :'))
                if findnode(desk) != None:
                    print('-'*40)
                    print('%-25s %-10s'%('Meal','Number'))
                    find_desk_meal(desk)
                    print('-'*40)
                    print('Total:',findnode(desk).total)
                else:
                    print('Desk %d no have order'%desk)
            elif option == 4:
                desk = eval(input('Enter which desk is delivered:'))
                delete_orl(desk)
            elif option == 5:
                show_meals()
            elif option == 6:
                modify_f()
            elif option == 7:
                calculate_deliver_time()
            #elif option == 8:
                #background_operation()
            elif option == 8:
                nearchainstore() 
            elif option == 9:
                data_output()
                Order_output()
                sys.exit(0) 
            else:
                print("不正確的選項")
    else:
        print('incorrect password !! ')
        print('please try again !!')



if __name__ == '__main__':
    main()