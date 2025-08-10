# program of dectionary having the odd key AND EVEN DATA
# ON GIVEN RANGE BY USER

def dect(start,end,dect={}):
    for i in range(start,end+1):
        if i % 2==1:
            dect[i]=i-1

    print(dect)

dect(int(input("Enter your starting point : ")),int(input("Enter your ending point : ")))
            
