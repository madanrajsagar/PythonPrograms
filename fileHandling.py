# file : file is used to store the data permanently ,whereas in our program the data remain for temporary basis..
# open(); open() method is used to open the file
''' here in following example that the  open() method must require one argument atleast , or you can define the mode as second argument 
 which is becuase the by defult mode is " r"  mode which meance read mode


'''
'''
# one thing also remember that the open() method return the object of specified file....
obj = open("abc.text","w")

obj.write("hello its my first file ...")

obj = open("abc.text")

print(obj.read())
'''






# folowing are the modes of file handling 

# 1. "r" : this mode is used to form thr read operation 
# 2. "w" : in this mode we can write the data but the existing data get deleted and then current data get replaced to it 
# 3. "a" : in this mode we can append the data present the exiting file , here data which is present would not get deleted but it get appended
# 4. "r+": in this mode  we can form both read as well as write operation ..
# 5. "rb": used to read the file data in binary form, and place the pointer at the bigining of the file
# 6."rb+": used to read as well as write the file data in binary form, and place the pointer at the bigining of the file 
# 7. "wb": used to write the data in file in binary form, if the file exist the existing data get overried by the current data
# 8. "w+":  in this mode  we can form both read as well as write operation , if the file exist the existing data get overried by the current data
# 9."wb+": used to read as well as write the file data in binary form, and place the pointer at the bigining of the file and if the file exist the existing data get overried by the current data
#10. "ab": in this mode we can append the data which is in binary form with the exiting file , here data which is present would not get deleted but it get appended
# 11."a+":in this mode we can append as well as read the data present the exiting file , here data which is present would not get deleted but it get appended, it would add the file pointer at the end of file
#12."ab+":in this mode we can append as well as read the data in binary form present the exiting file , here data which is present would not get deleted but it get appended, it would add the file pointer at the end of file






#  following are the methods used to perform specific opearation ..
'''
# 1. writelines() : when we want to write sequence of string in the file that time we use the writelines() method, we can store thestrings n list and then we can aslo pass that iterable object as argument..

obj = open("abc.text","w")
obj.writelines("hello  i am madanraj ! what about you ?"+ "hello i am karan..")

# we also store it in list
list = ["i am subhas!","so then what do i do","i don't care...!"]
obj.writelines(list)

obj = open( "abc.text")
print(obj.read())
'''
'''
# 2. readline() : this used to read the single line from your file , it will read the line on which line your file pointer is...
obj = open("abc.te xt","r")
print(obj.readline())
'''
''''
# 3. readlines() ;  this method  used to read the  all line from your file , it will read the file linr by line  and  return list of lines 
# and from the line on which line your file pointer is...
obj = open("abc.te xt","r")
print(obj.readlines())

'''
'''
# 4. reading the file using for -loop : it would read a single line for single iteration
obj = open("abc.te xt","r")
for i in  obj:
    print(i)

 '''   



'''
#*manupulation with file pointer :-

# 1.using seek() method :- this method used to set the file pointer at the specific position , remember this method will not work while peforming any kind of append opration 
 
obj = open("abc.text","r")
obj.seek(10); # it will start form index number five 
print(obj.read())

# 2. using the tell() method :- this method returns the current position of file pointer

obj = open("abc.text","r")
print(obj.tell())
obj.seek(10); # it will start form index number five 
print(obj.read())
print(obj.tell())

'''
# hello this wos the basics of file findling .... how's you experiance ......!
























