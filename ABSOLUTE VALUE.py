def absolute_value(num):

 if num >=0:
    return num
 else:
    return -num

num = int(input("enter your number: "))
print(f"absolute value of {num}: ",absolute_value(num))