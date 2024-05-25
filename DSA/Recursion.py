#factorial
'''
def factorial(n): 
    if n==0: 
        return 1
    else : 
        return n * factorial(n-1)
print(factorial(5))
'''

#Binary Search
'''
def binary_search(data,target,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if target==data[mid]:
            return True,low,high,mid
        elif target<data[mid]:
            return binary_search(data,target,low,mid-1),mid
        else:
            return binary_search(data,target,mid+1,high),mid

lst=[1,2,3,4,5,6,8,9,10]
print(binary_search(lst,8,1,10)) 
'''
# Factorise
'''
import sys
sys.setrecursionlimit(1000000000)

def factorise(num,i):
    if i<=num:
        if num%i==0:
            print(i)
            num=num//i
        else:
            i+=1
    factorise(num,i)

factorise(44,2)
'''
#sum of digits of number
'''
def rsum(num):
    if num!=0:
        digit=num % 10
        num=int(num/10)
        sum = digit + rsum(num)
    else:
        return 0
    return sum

x=rsum(345)
print(x)
'''
'''
#PaperSize
def papersize(i, n, len, b):
    if n!=0:
        print(f'A{i}: L={len}, B={b}')
        newB=len/2
        newL=b
        n-=1
        i+=1
        papersize(i,n,newL,newB)

papersize(0,7,1189,841)
'''

# fibbonaci
'''
def fibbo(old, current, n):
    if n>=1:
        new=old+current
        print(new,end="")
        n=n-1
        fibbo(current,new,term)
old=1
current=1
print(old)
print(current)
fibbo(old,current,13)

'''
#integer to binary
'''
import sys

def dectobinnary(n):
    r=n%2
    n=int(n/2)
    if n!=0:
        dectobinnary(n)
    print(r,end="\t")
sys.setrecursionlimit(10**6)
num=dectobinnary(5)
print(num)
print(5%2,2/2)
'''
#sum of first 25 natural number 
'''
def isum(n):
    if n==0:
        return 0
    else:
        s=n+isum(n-1)
        return s

x=isum(25)
print(x)
'''
#armstrong number
''' 
def count(n):
    if n==0:
        return 0
    return 1+count(n//10)

def armstrong(num,n):
    if num==0:
        return 0
    return ((num%10)**n)+armstrong((num//10),n)

def checkif(num):
    countd=count(num)
    arms=armstrong(num,countd)
    if arms==num:
        return "Is a Armstrong Number"
    else:
        return "Not a Armstrong Number"
    
d=checkif(123)
print(d)
'''
#fibonacci funstion
'''
def fibo(old,current,terms):
    if terms>=1:
        new=old+current
        print(f"{new}",end="\t")
        terms=terms-1
        fibo(current,new,terms)

old=1
current=1
fibo(old,current,15)
'''
#sum of first 5 natural numbers
'''
def sum(n=0):
    while n<=5:
        n+=1
    return n
d=sum()
print(d)
'''

#counting vowels in a string
'''
import sys
sys.setrecursionlimit(10**6)
def countvowel(n):
    i=0
    s=n[i].lower()
    if s in "aeiou":
        i+=1
        return 1+countvowel(n[i])
    
    else:
        i+=1
        return countvowel(n[i])
s=countvowel("Tanmay")
print(s)
'''
#def vowel(str):
#   l="aeiouAEIOU"
#    count=len([char for char in str if char in l])
#    print(count)

#vowel("Tanmay")


'''
l='tanmay'
print(count())
'''

#the 3 peg problem
import sys
sys.setrecursionlimit(10**4)
def peg(n,Origin,Destination,Auxiliary):
    if n==1:
        print(f"Moved disk {n} form {Origin} to {Destination}")

    peg(n-1,Origin,Auxiliary,Destination)    
    print(f'Moved disk {n} from {Auxiliary} to {Destination}')
    peg(n,Auxiliary,Destination,Origin)
    


peg(4,"Orign",'Destination',"Auxiliary")


    
    


#ATM
'''
balance=1000
def withdraw(amount):
    bal = amount-balance

    return "amount withdrawn",amount,"\n", "balance remaining",bal

def show_balance(balance):
    return balance

def add_balance(amount):
    bal=balance+amount

    return "amount added successfully",bal

def chaange_pin(pin):
    n=int(input("enter your original pin"))
    if n==1234:
        pin=int(input("enter new pin"))
        n=pin

pin=int(input("enter your pin"))
if pin==1234:
    print
'''
        


