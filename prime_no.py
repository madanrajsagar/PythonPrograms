# to find prime numbers
# prime number :- the number which only divisible by itself or by 1

num = int(input('Enter a number to cheak prime or not : '))
flag = 0
if num==1 or num==0:
    print(1,"and",0,"is not a prime number ...!")
else:
    for i in range(2,num):
        if num%i==0:
            flag =1
            break
    if flag == 1:
        print(num,"is not prime number..!")
    else:
        print(num,"is a prime number..!")

        



        
            
