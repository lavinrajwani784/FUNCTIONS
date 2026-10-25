def ispalindrome(string):
    left_pos=0
    right_pos=len(string)-1
    while (left_pos<=right_pos):
        if not string[left_pos]==string[right_pos]:
            return False
        left_pos+=1
        right_pos-=1
    return True

string = input("enter the word: ").lower()
if ispalindrome(string):
    print("yes it is a palindrome number")
else:
    print("no it is not a palindrome number")