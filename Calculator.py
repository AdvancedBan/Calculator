# ========================================================================
#                   Calculator v1.0 github.com/AdvancedBan
#                            Made by AdvancedBan
#                              @0xAdvancedBan
# ========================================================================

from decimal import Decimal
import os
import sys

os.system("cls")

#HELP
print("HELP :")
print("Addition = +")
print("Soustraction = -")
print("Multiplication = x")
print("Division = /")
print("")
print("")

#TYPE
type = input("Enter the type of calculation requested >> ")

#ADDITION
if type == '+':
    addition1 = input("Enter the first digit of your addition >> ")
    addition2 = input("Enter the second digit of your addition >> ")
    add1 = Decimal(f'{addition1}')
    add2 = Decimal(f'{addition2}')
    addresult = (add1+add2)
    print(addresult)
#SOUSTRACTION
elif type == '-':
    soustraction1 = input("Enter the first digit of your subtraction >> ")
    soustraction2 = input("Enter the second digit of your subtraction >> ")
    sous1 = Decimal(f'{soustraction1}')
    sous2 = Decimal(f'{soustraction2}')
    sousresult = (sous1-sous2)
    print(sousresult)
#MULTIPLICATION
elif type == 'x':
    multiplication1 = input("Enter the first digit of your multiplication >> ")
    multiplication2 = input("Enter the second digit of your multiplication >> ")
    multi1 = Decimal(f'{multiplication1}')
    multi2 = Decimal(f'{multiplication2}')
    multiresult = (multi1*multi2)
    print(multiresult)
#DIVISION
elif type == '/':
    division1 = input("Enter the first digit of your division >> ")
    division2 = input("Enter the second digit of your division >> ")
    divi1 = Decimal(f'{division1}')
    divi2 = Decimal(f'{division2}')
    diviresult = (divi1/divi2)
    print(diviresult)
else:
    print("The character entered is not recognized !")


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    answer = input("Do you want to restart this program ?")
    if answer.lower().strip() in "y yes".split():
        restart_program()