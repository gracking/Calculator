
print(' '*34,'calculator')
print(' '*32,'--------------')

def sum(x,y):
    s=float(x)+float(y)
    print(s)

def difference(x,y):
    d=float(x)-float(y)
    print(d)

def product(x,y):
    p=float(x)*float(y)
    print(p)

def quotient(x,y):
    q=float(x)/float(y)
    print(q)

def main():
    while True:
        x=input('enter ur first number')
        if x.isdigit()==True:
            pass
        else:
            print('enter a valid number ')
            continue
        y=input('enter ur second number')
        if y.isdigit()==True:
            pass
        else:
            print('enter a valid number ')
            continue
        print('what would u like to find with these numbers')
        print('1. sum')
        print('2. difference')
        print('3. product')
        print('4. quotient')
        print('please enter their respective serial number')
        c=input()

        if c=='1':
            sum(x,y)
            break

        elif c=='2':
            difference(x,y)
            break

        elif c=='3':
            product(x,y)
            break

        elif c=='4':
            quotient(x,y)
            break
        else:
            print('invalid serial number')
            continue
        
while True:
    main()
    while True:
        print('press "x" to close or "r" to use calculator again')
        a=input()
        if a=='r':
            break
        elif a=='x':
            break
        else:
            continue
    if a=='r':
        continue
    else:
        break
        

