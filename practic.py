def addition(a,b=10):#example of default argument
    print("Addition of two numbers = ",a+b)
addition(10)

def substraction(*arg):#arbitrary argument
    print(arg)
    print(type(arg))

substraction(10,20,30)

def main(**dect):
    print(dect)
    print(type(dect))

main(a="yash",b="kumar",c="gandu")#keyword args


#@ qa. take input from use range(start and end), and find out even numbers
#from that and save it as key for dictionary and take
#key'sqare to there vaalue

    def main(start,end,dect = {}):
    for i in range(start,end+1,2):
        if i%2==0:
            dect[i] = i*i 
    return dect
a = isb = int(input("enter ennding point of your range : "))
print(main(a,b))














