# program to find maximum number from three numbers using fuction

def max(a,b,c):
    if(a>b and a>c):
        print("a is greater..!")
    elif(b>a and b>c):
        print("b is greater...!")
    else:
        print("c is greater ...!")

max(int(input("enter your first value : ")),int(input(
    "Enter the second value : ")),int(input("Enter the thired value :")))
