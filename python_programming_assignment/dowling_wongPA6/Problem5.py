# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #6
#
# Description: Write a program that produces a Caesar cipher of a given message string. A Caesar cipher is
#formed by rotating each letter of a message by a given amount. For example, if your rotate by 3,
#every A becomes D; every B becomes E; and so on. Toward the end of the alphabet, you wrap
#around: X becomes A; Y becomes B; and Z becomes C. Your program should prompt for a
#message and an amount by which to rotate each letter and should output the encoded message.

def main():
    txt=input("Please input a string you want to convert: ")
    num=int(input("please give an amount you want to rotate: "))
    ceaconvert(txt,num)
    
def ceaconvert(x,y):
    for i in range (len(x)):
        char=x[i]
        if ord(char)>64 and ord(char)<91:
            #This step is to check whether it is a upper letter or lower letter
            char=chr((ord(char)+y-65)%26+65)
        if ord(char)>96 and ord(char)<123:
            char=chr((ord(char)+y-97)%26+97)
        else:
            #If the input is neither upper nor lower, we keep it as initial one
            char=char
        print(char,end="")
        
main()
