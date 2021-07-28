#import time

print("This is an intial file")

l = [1,2,3,4,5]

def list_output(l):
    n=0
    for i in l:
        if i>2:
            print("Greater than the first prime number")
            n=n+1

    return ("There are %s numbers in this list which are greater than 2", n)

#This is a test file

