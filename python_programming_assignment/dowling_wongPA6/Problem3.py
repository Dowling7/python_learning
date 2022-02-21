# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #6
#
# Description: Write a program that determines if a string is palindrome. A palindrome string is a string that
#reads the same backward as forward. For example: “ABA”, “madam”, “abba”. Prompt the user
#for a string and validate if the string is a palindrome. Your program should return True if the
#string is palindrome, False otherwise. Assume the string the user entered has no punctuations and
#spaces.

def main():
    s = input("Please input a string that you want to test")
    answer = isPalindrome(s)
    if (answer):
        print("Yes")
    else:
        print("No")

# palindrome or not
def isPalindrome(str):
# Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

main()
