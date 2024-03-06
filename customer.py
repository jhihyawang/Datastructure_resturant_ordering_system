import sys
import Order

class Member:
    def __init__(self):
        self.llink = None
        self.id = 0
        self.name = ''
        self.count = 0
        self.password = 0
        self.rlink = None

class Orders:
    def __init__(self):
        self.meal = None
        self.rlink = None
        self.llink = None
        self.total = 0
        self.member = None
        self.desk_number = 0
        
class Meal:
    def __init__(self):
        self.next = None
        self.ID = 0
        self.name = ''
        self.price = 0
        self.number = 0

head = Member()
head.id = 0
head.name = ''
head.count = 0
head.password = 0
head.llink = head
head.rlink = head 

oroot = None
#################### Member part###############################
def add_member():
    id =int(input('digits Member ID : '))
    if search_member(id) != None:
        print('\nmember id is exist!!\n')
        return
    if len(str(id)) != 4:
        print("Member id must be 4 digits nummber !")
        print("try again\n")
        return

    password = eval(input('Member Password: '))
    name = input('Member name:')
    count = 0
    access(id,password,name,count)


def access(id,password,name,count):
    global head
    ptr = Member()
    if search_member(id) != None:
        print('\nmember id is exist!!\n')
        return
    ptr.id = id
    ptr.password = password
    ptr.name = name
    ptr.count = count
    prev = head
    current = head.rlink
    while current != head and current.count >= ptr.count:
        prev = current
        current = current.rlink
    ptr.rlink = current
    ptr.llink = prev
    prev.rlink = ptr
    current.llink == ptr

def del_member(id):
    global head
    prev = head
    current = head.rlink
    while current != head and id != current.id:
        prev = current
        current = current.rlink

    if head != current:
        prev.rlink = current.rlink
        current.rlink.llink = prev
        current = None
        #print('Member %s Has Been Deleted!! \n' % id)

def del_allmember():
    global head
    prev = head
    current = head.rlink
    while current != head:
        member = search_member(current.id)
        del_member(member.id)
        prev = current
        current = current.rlink
        
def search_member(search_id):
    global head
    prev = head
    current = head.rlink
    while current != head and search_id != current.id:
        prev = current 
        current = current.rlink

    if current != head:
        return current
    else:
        return None 

def login_f():
    id = eval(input('\nEnter member id:'))
    member = search_member(id)
    if search_member(id) == None:
        print('Member is not exist!!')
        print('Please try again or sign up !!')
        return
    password = eval(input('Enter member password:'))
    if password == search_member(id).password:
        member = search_member(id)
        print('log in success')
        option = 0
        while True:
            print("\n************* Choose a service ****************")
            print('-------- Member data --------')
            print('\nMember id: %d'%(member.id))
            print('Member name: %s'%(member.name))
            print('Member password: %d'%(member.password))
            print('Remain point:%d'%(member.count))
            print('-----------------------------')
            print("<1>Order dish")
            print("<2>Setting")
            print("<3>log out")
            print("***********************************************")
            try:
                option = int(input("   Choice ： "))
            except ValueError:
                print("Not a correct number.")
                print("try again\n")

            print()
            if option == 1:
                order_dish(member)
            elif option ==2:
                setting_f(id)
            elif option == 3:
                break
            else:
                print("不正確的選項")
    else:
        print('password is uncorrect')
        print('Please try again or change password')
        return 

def setting_f(id):
    while True:
        print("\n***************** Setting *********************")
        print("<1>change information")
        print("<2>delete member")
        print("<3>back")
        print("***********************************************")
        try:
            option = int(input("   Choice ： "))
        except ValueError:
            print("Not a correct number.")
            print("try again\n")

        print()
        if option == 1:
            modify_f(id)

        elif option ==2:
            del_member(id) 
            print('Member %s Has Been Deleted!! \n' % id)
            print('Bye Bye !!')
            data_output()
            sys.exit(0)

        elif option == 3:
            break
        else:
            print("不正確的選項")     
    
    
def modify_f(id):
    #global head
    #prev = head
    #current = head.rlink
    #while current != head and id != current.id:
    #    prev = current
    #    current = current.rlink

    #顯示原始資料
    member = search_member(id)
    print('--------Original data--------')
    print('Member id: %d'%(member.id))
    print('Member name: %s'%(member.name))
    print('Member password: %d'%(member.password))
    print('-----------------------------')
            
    #刪除原始資料
    #prev.rlink = current.rlink
    #current.rlink.llink = prev
    #current.next = None
    
    while True:
        print('1.modify id')
        print('2.modify name')
        print('3.modify password')
        print('4.back')
        try:
            op = eval(input('Enter the requirment:'))
            print('-'*40)
        except ValueError:
            print("Not a correct number.")
            print("try again\n")
        if op == 1:
            newid = eval(input('Enter new id : '))
            member.id = newid
            print('change id success')
            print('-'*40)
        if op == 2:
            newname = input('Enter new name : ')
            member.name = newname
            print('change name success')
            print('-'*40)
        if op == 3:
            newpassword = eval(input('Enter new password : '))
            member.password = newpassword
            print('change password success')
            print('-'*40)
        if op == 4:
            break

    #ptr = Member()
    #ptr.next = None
    #ptr.id = current.id
    #ptr.name = current.name
    #ptr.count = current.count
    #ptr.password = newpassword
    #prev = head
    #current = head.rlink
    #while current != head and current.count >= ptr.count:
    #    prev = current
    #    current = current.rlink
    #ptr.rlink = current
    #ptr.llink = prev
    #prev.rlink = ptr    

def data_input():
    f = open('member.txt','r')
    print("start insert data")
    while True:
        id = f.readline().strip()
        name = f.readline().strip()
        count = f.readline().strip()
        password =f.readline().strip()
        if id != '' and name != '' and count != '':
            access(int(id),int(password),name,int(count))
            #print(int(id),int(password),name,int(count))#check
            
        if f.readline() == '':
            f.close()
            print("data reading success")
            return

def data_output():
    global head
    path = 'member.txt'
    if head.rlink == head:
        #print('\nNo member record !!\n')
        with open(path,'w') as f:
            f.close()
        print("data writing.....")
    else:
        with open(path,'w') as f:
            current = head.rlink
            while current != head:
                f.write(str(current.id)+'\n')
                f.write(current.name+'\n')
                f.write(str(current.count)+'\n')
                f.write(str(current.password)+'\n')
                f.write('\n')
                #print(current.id,current.name,current.count,current.password)
                current = current.rlink
        f.close() 
        print("data writing.....")

############# only for demo
def display_f():
    global head
    count = 0
    if head.rlink == head:
        print('\n    No member record !!\n')
    else:
        print('\n%-10s %-10s %-10s %-10s'%('ID','NAME','POINT','password'))
        print('----------------------------------------------------------')
        current = head.rlink
        while current != head:
            print('%-10d %-10s %-10d %-10d'%(current.id,current.name,current.count,current.password))
            count+=1
            current = current.rlink
        print('----------------------------------------------------------')
        print('There is %d member(s) !!\n'%(count))
    
##################### Order part ############################
def order_dish(member):
    o = Order.Order()
    o.build_menu()
    o.show_menu()
    option = 0
    mhead = Meal()
    print()
    desk_number = int(input("Enter desk number(1~7) ： "))
    order = Orders()
    while option!=3:
        print("\n***************************************")
        print("<1>choose meals")
        print("<2>modify meals")
        print("<3>finish")
        print("<4>show ordered meals")
        print("***************************************")
        try:
            option = int(input("   Choice ： "))
        except ValueError:
            pass
        
        print()
        if option == 1:
            add_meal(o,mhead)
        elif option ==2:
            modify_meal(o,mhead)
        elif option == 3:
            add_order(order,mhead,member,desk_number)
            inorder_orders(oroot)
            Order_output(order)
        elif option == 4:
            show_meals(mhead)
        else:
            print('incorrect choice !!')

def add_meal(o,mhead):
    choose = -1
    number = 0
    con = ''
    o.show_menu()
    while con!='n':
        choose =eval(input('Choose meal : '))
        if o.search(choose)==None:
            print("Meal not found")
        else:
            number = eval(input('number : '))
            m = Meal()
            m.name = o.search(choose).name
            m.price = o.search(choose).price
            m.number = number
            ptr = mhead
            ID = 1
            while ptr.next:
                ptr = ptr.next
                ID+=1
            ptr.next = m
            m.ID = ID
        show_meals(mhead)
        con =input('Continue?(y/n) : ')
        o.show_menu()

def modify_meal(o,mhead):    
    choose = -1
    con = ''
    while con!='n':
        if show_meals(mhead)==None:
            break
        choose =eval(input('Choose modify meal ID : '))
        ptr = mhead.next
        while ptr.ID!=choose:
            ptr = ptr.next 
            if ptr==None:
                print("Not found meal")
                break
        if ptr!=None:
            print("\n***************************************")
            print("<1>modify number")
            print("<2>delete")
            print("***************************************")
            choose =eval(input('Choose : '))
            if choose == 1:
                modify_number(mhead,ptr)
            elif choose ==2:
                delete_meal(mhead,ptr)
            else:
                print("Not found choice")
            show_meals(mhead)    
            con =input('Continue?(y/n) : ')


def show_meals(head):
    if head.next == None:
        print("No meals")
        return None
    ptr = head.next
    total = 0
    print('-'*30)
    while ptr:
        print(ptr.ID,ptr.name,ptr.price,'*',ptr.number)
        total += (ptr.price*ptr.number)
        ptr = ptr.next 
    print('\ntotal : %d' % total)
    print('-'*30)
    return 1


def add_order(order,meals,member,desk_number):
    global oroot
    prev = None
    node = None
    mptr = meals.next
    total = 0
    print('-'*30)
    while mptr:
        total += (mptr.price*mptr.number)
        mptr = mptr.next 
    ptr = order
    ptr.desk_number = desk_number
    ptr.meal = meals
    ptr.member = member
    ptr.total = total

    if oroot==None:
        oroot = ptr
    else:
        node = oroot
        while node!=None:
            prev = node
            if ptr.total < node.total:
                node = node.llink
            else:
                node = node.rlink
        if ptr.total < prev.total:
            prev.llink = ptr
        else:
            prev.rlink = ptr    

def modify_number(mhead,meal):
    number = eval(input('change number : '))
    if number<=0:
        delete_meal(mhead, meal)        
    meal.number = number

def reset_ID(head):
    ptr = head.next
    ID = 1
    while ptr:
        ptr.ID = ID
        ptr = ptr.next
        ID+=1
    
def delete_meal(head,meal):
    prev = head
    cur = head.next
    while cur:
        if cur.ID == meal.ID:
            prev.next = cur.next
            cur =None
            reset_ID(head)
            return
        prev = cur
        cur = cur.next
    print('Not Found Meal')

def inorder_orders(node):
    if node!=None:
        inorder_orders(node.llink)
        node.member.count+=((node.total)//100)
        print('Desk : %d,Total is %d ,Customer is %s ,get %d point'%(node.desk_number,node.total,node.member.name,((node.total)//100)))
        inorder_orders(node.rlink)

def Order_output(order):
    file = open('order.txt','a')
    ptr = order.meal.next
    total = 0
    print('-'*30)
    file.write(str(order.desk_number)+'\n')
    while ptr:        
        file.write(str(ptr.ID)+',')
        file.write(ptr.name+',')
        file.write(str(ptr.price)+',')
        file.write(str(ptr.number))
        file.write('\n') 
        total += (ptr.price*ptr.number)
        ptr = ptr.next 
    file.write('##')
    file.write('\n')
    file.write(str(total)+'/')
    file.write('\n')
    print('Order is writting.....')

####################################################################

def main():
    option = 0
    data_input()
    while True:
        print("\n************** Order dish system **************")
        print("<1>sign up")
        print("<2>log in")
        print("<3>exit")
        print("***********************************************")

        try:
            option = int(input("   Choice ： "))
        except ValueError:
            print("Not a correct number.")
            print("try again\n")

        print()
        if option == 1:
            add_member()
        elif option ==2:
            login_f()
        elif option == 3:
            data_output()
            del_allmember()
            break
        elif option == 4:
            display_f() #### hiding choice ######
        else:
            print("不正確的選項")
            
if __name__ == '__main__':
    main()
