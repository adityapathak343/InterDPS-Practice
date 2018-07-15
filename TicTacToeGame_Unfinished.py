#defining grid and other funcrtions
from os import system, name
a = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
a1 = [1,2,3,4,5,6,7,8,9]
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
def wfx():
    if ((a[0] == 'X' and a[1] == 'X' and a[2] == 'X')or(a[3] == 'X' and a[4] == 'X' and a[5] == 'X')or(a[6] == 'X' and a[7] == 'X' and a[8] == 'X')or(a[0] == 'X' and a[3] == 'X' and a[6] == 'X')or(a[1] == 'X' and a[4] == 'X' and a[7] == 'X')or(a[2] == 'X' and a[5] == 'X' and a[8] == 'X')or(a[0] == 'X' and a[4] == 'X' and a[8] == 'X')or(a[2] == 'X' and a[4] == 'X' and a[6] == 'X')):
        print('X has won!')
        raise SystemExit
def wfy():
    if ((a[0] == 'O' and a[1] == 'O' and a[2] == 'O')or(a[3] == 'O' and a[4] == 'O' and a[5] == 'O')or(a[6] == 'O' and a[7] == 'O' and a[8] == 'O')or(a[0] == 'O' and a[3] == 'O' and a[6] == 'O')or(a[1] == 'O' and a[4] == 'O' and a[7] == 'O')or(a[2] == 'O' and a[5] == 'O' and a[8] == 'O')or(a[0] == 'O' and a[4] == 'O' and a[8] == 'O')or(a[2] == 'O' and a[4] == 'O' and a[6] == 'O')): 
        print('O has won')
        raise SystemExit
prgrd()
ctr = 1

#maincode:
a = [1,2,3,4,5,6,7,8,9]
prgrd()
a = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print("Press any key to play!..")
input()
clear()
prgrd()
ctr=1
while(ctr < 9):
    x = int(input("Where would you like to place X? "))
    if x in a1:
        if a[x-1] != ' ':
            print("Invalid Input. Exiting!")
            raise SystemExit
        a[x-1] = 'X'
    clear() 
    prgrd()
    wfx()
    o = int(input("Where would you like to place O? "))
    if o in a1:
        if a[o-1] != ' ':
            print("Invalid Input. Exiting!")
            raise SystemExit
        a[o-1] = 'O'
    clear() 
    prgrd()
    wfy()
    ctr = ctr + 1
print("The match was tied!")