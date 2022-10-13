n = int(input('Enter number\n'))
def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
            break
    if c==1:
        print('Not Prime')    
    else:
        print('Prime')  
prime(n)          
