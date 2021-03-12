#2 Rotate the characters in a string by a given input and have the overflow appear at the beginning, 
# e.g. “MyString” rotated by 2 is “ngMyStri”
def rotateChr(s, num):
    s1 = s[-num:]
    s2 = s[0:-num]
    print(s1+s2)
    
# s = "abcd"
# num = 3
s ="MyString"
num =2
# s = ""
# num = 1
# s = " asfbc "
# num = 3
# s = "aksb#ksfdblkaf*oihdb*a2"
# num = 8

rotateChr(s ,num) 