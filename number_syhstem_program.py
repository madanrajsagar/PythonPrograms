#program to convert digits to its binary
#mine logic
def numberSystem():
    res = ""
    num = int(input("Enter thrb number to be converted : "))
    temp = num
    while num>0:
        rem = str(num%2)
        res = res+rem
        num = num//2 # floor division operator

    print("The binary number of ",temp," : ",int(res[::-1]))


numberSystem()
'''
# program by second way

def numberSystem():
    num = int(input("Enter the number to be converted: "))
    
    # Initialize variables
    res = 0
    place = 1
    
    # Convert the number to binary
    while num > 0:
        rem = num % 2
        res = res + rem * place
        num = num // 2
        place = place * 10
    
    print("The binary number of", num, ":", res)

numberSystem()

      

'''
