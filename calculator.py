dict={'1':['add','sum'],'2':['subtract','difference'],'3':['multiply','product'],'4':['divide','quotient']}
print(' '*34,'CALCULATOR')
print(' '*32,'--------------')

while True:
    while True:
        #main
        print('What would you like to find:')
        print('1. Sum')
        print('2. Difference')
        print('3. Product')
        print('4. Quotient')
        c=input('Please enter their respective serial number : ')


        if c not in ['1','2','3','4']:
            print('Enter a valid number.')
            continue
        l=[]
        b=input(f'How many numbers would you like to {dict[c][0]}.')


        if b.isdigit()==True:
            if int(b)==0:
                print('You cant do anything with zero numbers here.')
                continue
            pass
        else:
            print('Enter a number')
            continue
        if int(b)==0:
            continue

      
        for i in range(int(b)):
           while True:
                n=input(f'Enter  no.{i+1} : ')
                if n.isdigit()==True:
                    if c=='4':
                        if n=='0':
                            if i !=0:
                                print('You cant divide a number by zero.')
                                continue
                    l.append(n)
                    break
                else:
                    print('Enter a number.')
                    continue


        print(f'The {dict[c][1]} is',end=' ')

       #sum 
        if c=='1':
            s=0
            for i in range(len(l)):
                s+=float(l[i])
            print(s)
            break
        #difference
        elif c=='2':
            d=0
            for i in range(1,len(l)):
                d+=float(l[i])
            d=float(l[0])-d
            print(d)
            break
        #product
        elif c=='3':
            p=1
            for i in range(len(l)):
                p*=float(l[i])
            print(p)
            break
        #quotient
        elif c=='4':
            q=1
            for i in range(1,len(l)):
                q*=float(l[i])
            q=float(l[0])/q
            print(q)
            break

        
    while True:
        a=input('Press "x" to close or "r" to use calculator again : ' )
        if a.lower()=='r':
            break
        elif a.lower()=='x':
            break
        else:
            continue
    if a.lower()=='r':
        continue
    else:
        break
        

