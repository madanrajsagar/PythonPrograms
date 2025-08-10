# program to count no. of uppercase leters and lowercase

def countletter(l=0,u=0):
    s = input("Enter your string : ")
    for i in s:
        if i.isupper():
            u = u+1
        elif i.islower():
            l = l+1

        else:
            pass
    print("Totle uppercaseletter : ",u)
    print("Totle lowercaseletter : ",l)

countletter()
