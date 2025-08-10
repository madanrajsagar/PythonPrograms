# program to reverse the given string
def reverse_str(str1):
    last = len(str1)-1
    first = 0
    reverse =" "
    for i in range(0,len(str1)+1):
        reverse[first] =str1[last]
        first = first+1
        last = last-1

    return reverse
str1 =input("enter a string to reverse it:")
print(reverse_str(str1))
