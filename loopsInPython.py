name = {}
Class= {}

ans = 'y'

while ans == 'y':
    no= int(input("enter no. of students data you want to add : "))
    for i in range(1,no+1):
        n = input("enter the name of student : ")
        c = input("enter the class of that student : ")

        name[i]= n
        Class[i]=c

    ans= input(" do you want to add more (y/n):  ")
print(name)
print(Class)

student= {}

student = {1:name,2:Class}
print(student[2])
