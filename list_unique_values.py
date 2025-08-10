#wap to take one list with duplicate values and print that
#list with distict value

def find_distict_value(list):
    uni_list = []
    for i in list:
        if i not in uni_list:
            uni_list.append(i)            
        
    return uni_list
list = [10,10,10,20,20,20,30,40,50]
print(find_distict_value(list))            

"""
Note :- always remember while conding in python ,while
        handling the sequential data always give first
        priority to the methods can be applied on that
        datatype's value..


        
        
