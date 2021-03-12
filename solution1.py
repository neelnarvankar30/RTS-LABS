# 1 Print the number of integers in an array that are above the given input and the number that are below, 
# e.g. for the array [1, 5, 2, 1, 10] with input 6, print “above: 1, below: 4”.

def printNums(arr, num):
    high = 0
    low = 0
    
    for i in arr:
        if i < num:
            low += 1
        elif i > num:
            high += 1
    print("above:", high,"below:", low)
       
arr = [1, 5, 2, 1, 10]
num = 6
# arr = []
# num = 10
# arr = [-6,1, -2, 50]
# num = -2

printNums(arr , num)       