def sum():
    num = int(input())
    sum = 0
    while True:
        if num != 0:
            sum+=num
            num = int(input())
        else:
            print(sum)
            break    

def devide():
    num1 = int(input())
    num2 = int(input())
    while True:
        if num2 != 0:
            num1-=num2
            num2 = int(input())
        else:
            print(num1)
            break            


print("------------------mini calculator------------------")        
print()
print("Enter your choice :")
print(">>press 1 for sum \n>>press 2 for divide")
choice = int(input("choice:"))
if choice == 1:
    sum()
elif choice == 2:
    devide()    
