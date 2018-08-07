#defining grid and other funcrtions
from os import system, name
import random
ctr=0
p = [False,False,False,False,False,False,False,False,False]
c = [False,False,False,False,False,False,False,False,False]
a = [1,2,3,4,5,6,7,8,9]
def prgrd():
    print(" _________________")
    print("|     |     |     |")
    print("| ",a[6]," | ",a[7]," | ",a[8]," |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("| ",a[3]," | ",a[4]," | ",a[5]," |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("| ",a[0]," | ",a[1]," | ",a[2]," |")
    print("|_____|_____|_____|")
def clear():
    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')
def wfp(l):
    if c[l-1] == True:
        print('You won!')
        a[l-1]='🚀'
        prgrd()
        raise SystemExit
    else:
        a[l-1]='X'
        print("You missed!")
def wfc(o):
    if p[o]==True:
        print("The computer won")
        raise SystemExit
    else:
        print("The computer missed. Your turn!")
#BEGIN GAME
prgrd()
input("Ready to begin? Hit enter!...")
xpos=int(input("Where would you like to place your ship?.."))
p[xpos-1]=True
cpos=random.randint(0,8)
c[cpos]=True
while (ctr<=9):
    clear()
    prgrd()
    pc=int(input("Where would you like to attack?"))
    wfp(pc)
    cc=random.randint(0,8)
    wfc(cc)
    ctr=ctr+1
    