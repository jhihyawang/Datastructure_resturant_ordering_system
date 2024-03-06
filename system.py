import customer
import staff
import sys

def main():
    option = 0
    while True:
        print("\n********** Welcome NCHU restaurant !! **********")
        print("<1> I am customer ")
        print("<2> I am staff ")
        print("<3> EXIT ")
        print("************************************************")
        try:
            option = int(input("   Choice ： "))
        except ValueError:
            print("Not a correct number.")
            print("try again\n")
        
        print()
        if option == 1:
            customer.main()
        elif option ==2:
            staff.main()
        elif option == 3:
            sys.exit(0)  
        else:
            print("不正確的選項")

main()