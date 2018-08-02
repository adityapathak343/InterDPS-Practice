#simplification: bottom to top
def itw(x):
    s=''
    l=len(x)-1
    ones=['','one', 'two', 'three', 'four', 'five', 'six','seven','eight','nine']
    tens=['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    ltens=['ten', 'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    suff=['',tens[int(x[-2])], 'hundred and','thousand', '']
    for letter in x:
            s=ones[int(letter)]+" "
            if l == 1:
                s=''
                if int(x[-2])==1:
                    s=''
                    print(ltens[int(x[-1])])
                    exit
            t = suff[l]
            if s==' ' and l==2:
                t='and'
                if int(x[-1]) == 0:
                    t=''
            print (s+t, end=" ")
            l=l-1     
            if l<0:
                exit       
y  = input("Enter a number..")
itw(y)