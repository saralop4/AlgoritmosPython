import math 
import os
os.system("cls")
num= int(input("numero a invertir: "))

def rev(num): 
    while(num>0):
        inv=0
        inv=inv* 10 + (num % 10)
        num = num // 10
        print("inv: ",inv)
        print("num: ",num)

    return inv

    
if(rev(num)==num):
            print(num," is a palindrome")
    
else:
    print(num," is NOT a palindrome") 
    