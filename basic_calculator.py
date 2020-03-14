"""
Please select operation -
1. Add
2. Subtract
3. Multiply
4. Divide
Select operations form 1, 2, 3, 4 : 1
Enter first number : 20
Enter second number : 13
20 + 13 = 33
"""

def add(n1,n2):
    add = n1+n2;
    print("addition of two no is ", add)
def sub(n1,n2):
    sub = n1-n2;
    print("sub of two no is ", sub)
def mul(n1,n2):
    mul = n1*n2;
    print("mul of two no is ", mul)
def div(n1,n2):
    div = n1/n2;
    print("div of two no is ", div)


def main():

    select = int(input("Select a number to perform basic operations: \n"\
                       "1. 1 is for add \n"\
                       "2. 2 is for sub \n"\
                       "3. 3 is for mul \n"\
                       "4. 4 is for div \n "))
    n1 = int(input("enter first number "))
    n2 = int(input("enter second number "))
    if (select == 1):
        add(n1,n2)
    elif(select == 2):
        sub(n1,n2)
    elif (select == 3):
        mul(n1,n2)
    elif (select == 4):
         div(n1,n2)

main()