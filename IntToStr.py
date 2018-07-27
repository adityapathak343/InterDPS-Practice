#simplification: bottom to top
ones=['zero','one', 'two', 'three', 'four', 'five', 'six','seven','eight','nine']
suff=['ones','tens', 'hundreds','thousands','millions']
def inv(s):
    st=""
    for letter in s:
        st=letter+st
    return st
def itw(x):
    s=''
    for letter in x:
        s+=ones[int(letter)]+""
    print(s)
y  = input("Enter a number..")


itw(y)


