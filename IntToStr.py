#simplification: bottom to top
def inv(s):
    st=""
    for letter in s:
        st=letter+st
    return st
def itw(x):
    s=''
    l=len(x)-1
    ones=['','one', 'two', 'three', 'four', 'five', 'six','seven','eight','nine']
    tens=['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    ltens=['ten', 'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    suff=['',tens[int(x[len(x)-2])], 'hundred and','thousand', '']
    for letter in x:
            s=ones[int(letter)]+" "
            if l == 1:
                s=''
                if int(x[len(x)-2])==1:
                    s=''
                    print(ltens[int(x[len(x)-1])])
                    raise SystemExit
            t = suff[l]
            if s==' ':
                t='and'
            print (s+t, end=" ")
            l=l-1     
            if l<0:
                raise SystemExit       
y  = input("Enter a number..")
itw(y)
