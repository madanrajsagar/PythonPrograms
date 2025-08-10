# program to find out percentage using class constructor

class Find_percent :
    def __init__(self,n,list):
        self.total_marks = n*100
        self.obtained_marks = sum(list)
        self.perecentage = (self.obtained_marks/self.total_marks)*100

        print(self.perecentage)
        
        
    
num = int(input("Enter no. of subjects : "))
list =[]
for i in range(num):
    marks = int(input("Enter your marks "))
    list.append(marks)
Find_percent(num,list)

'''

# my result
    
percent = ((445+60+60+60+60)/750)*100
print(percent)
'''
